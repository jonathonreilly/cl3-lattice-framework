#!/usr/bin/env python3
"""Finite spin-1/2 link-model components, winding classes and pair-update parity.

The mathematical model and two geometries are supplied. This is a standalone
NumPy/SciPy calculation with an embedded C sampler, not a physical Record law.
A: all 9600 Gauss states, 937 flip components, 125 cut-flux winding classes,
   and finite full/component spectral gaps (observable overlap is separate).
B: exact same-face pair parity, cycle-image ranks 0/10 and legal closed walks.
C: complete finite-component thermal references on the L8 ladder and 2x2x2 torus.
D: original seeded energy/bin witnesses, cumulative invariant diagnostics,
   bounded Gauss checkpoints and the equal-time E_e^2=1/4 identity only.
E: geometric six-face factor (not acceptance), restricted-sampler timing,
   finite spectral distinctions and an executable source/readout scope check.

All 21 original check IDs are retained. Required compiler/engine/data failures
are failures of the complete unit, never successful skipped evidence. Exact
integer statements, numerical spectral tolerances, seeded diagnostics and
source declarations are distinguished. Original seeds, budgets, estimators,
updates and random draws remain; added Gauss checks draw no random numbers.
The positive-lag time-array/indexing implementation is not validated here.
No thermal mass, mixing time, infinite-size phase, physical photon or universal
sampler necessity follows from the finite parity obstruction. The procedural
five-route no-go packet minimum is unmet; no packet/audit PASS is asserted.
"""

from __future__ import annotations

import math
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import Counter, deque
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.sparse.csgraph import connected_components

AUDIT_TIMEOUT_SEC = 150
AUDIT_INPUT_PATHS = (
    "docs/THE_LINK_MODELS_PAIR_UPDATE_CONSERVES_PLAQUETTE_PARITY_AND_THE_2X2X2_GAUSS_SECTOR_SPLITS_INTO_937_WINDING_COMPONENTS_BOUNDED_THEOREM_NOTE_2026-09-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
SEED = 20260903
LAM = 1.0
DENSE_MAX = 2500
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_SHA256 = "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753"

def source_scope_certificate():
    note = NOTE_PATH.read_text()
    memo = (ROOT / AUDIT_INPUT_PATHS[1]).read_bytes()
    required = (
        "125 winding classes", "937 plaquette-flip connected components",
        "positive-lag implementation remains unvalidated",
        "five-route procedural minimum is unmet",
        "formal audit remains deferred", "not a physical Record formation law",
    )
    return (hashlib.sha256(memo).hexdigest() == AXIOM_SHA256
            and all(phrase in note for phrase in required))

T0 = time.time()
PASS = 0
FAIL = 0
SKIPPED = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


def skip(label):
    """Record and print one skipped check; counted in neither PASS nor FAIL."""
    global SKIPPED
    SKIPPED += 1
    print("SKIP " + label)


def v0_of(n):
    """Deterministic Lanczos start: equidistributed, no symmetry, no seed."""
    v = np.cos(np.arange(n, dtype=float) * np.sqrt(2.0)) + 1.5
    return v / np.linalg.norm(v)


def low_spectrum(H, nev):
    """Lowest nev levels and vectors of a sparse symmetric H, dense below DENSE_MAX."""
    n = H.shape[0]
    if n <= DENSE_MAX:
        w, v = np.linalg.eigh(H.toarray())
        return w[:nev], v[:, :nev]
    k = min(nev + 6, n - 2)
    w, v = spla.eigsh(H, k=k, which="SA", v0=v0_of(n), maxiter=20000, tol=0.0)
    o = np.argsort(w)
    return w[o][:nev], v[:, o][:, :nev]


# The original embedded sampler with deterministic Gauss/diagnostic guards.
# No added check draws random numbers or changes the update/measurement algorithm.

SSE_C = r"""/* P1 -- stochastic series expansion for the pure spin-1/2 U(1) quantum link model
 *      H = -lambda sum_f P_f ,   P_f = W_f + W_f^dag  (four-link ring exchange)
 *
 * SSE construction.  Put  H_{1,f} = C * I  (diagonal, weight C, applicable always)
 *                        H_{2,f} = lambda * P_f  (off-diagonal, weight lambda when
 *                                                 plaquette f is flippable)
 *   K = sum_f (H_{1,f}+H_{2,f})  =>  H = NP*C - K  and  Z = e^{-b NP C} Tr e^{bK}.
 *   Fixed-length-M expansion with identity padding:
 *      W = beta^n (M-n)!/M! prod_p <a(p)|H_{a_p,b_p}|a(p-1)>.
 *   Estimators:  E = NP*C - <n>/beta ;  <P_f> = <n_2>/(NP*beta*lambda) ;
 *                Cv = <n^2>-<n>^2-<n>.
 *
 * Updates
 *   (a) diagonal insert/remove of H_{1,f}.  H_{1,f}=C*I is state-INDEPENDENT, which
 *       is exactly what makes (b) legal inside the same forward pass.
 *   (b) off-diagonal PAIR SWITCH: for two CONSECUTIVE operators at the same plaquette
 *       f, positions pp<p, with NO off-diagonal operator on any link-sharing
 *       plaquette strictly between them, switch both between type 1 and type 2.
 *       The net action over [pp,p] is preserved so a(q) for q>=p is untouched; the
 *       states in between get f's four links flipped, which no operator in the window
 *       can see (diagonal ops are state-independent).  Involution + symmetric
 *       legality test => detailed balance move by move.
 *   (c) uniform random cyclic rotation of the padded string (an exact symmetry of the
 *       SSE weight).  This is a weight-preserving boundary-state move; it does not
 *       prove complete sampling of a trace ensemble.
 *
 * Imaginary time: operator j gets the j-th order statistic of n uniforms on [0,beta)
 * (n+1 exponential spacings). The distributional construction is exact;
 * the stored-array and positive-lag indexing implementation remains unvalidated.
 *
 * The QMC never leaves the connected component of the plaquette-flip graph that
 * contains the initial configuration. Winding labels need not identify a
 * unique connected component, and observable decay need not equal its first gap.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

/* ------------------------------------------------------------------ rng */
static uint64_t rs[4];
static inline uint64_t rotl(const uint64_t x,int k){ return (x<<k)|(x>>(64-k)); }
static inline uint64_t nextr(void){
    const uint64_t r=rotl(rs[1]*5,7)*9, t=rs[1]<<17;
    rs[2]^=rs[0]; rs[3]^=rs[1]; rs[1]^=rs[2]; rs[0]^=rs[3]; rs[2]^=t;
    rs[3]=rotl(rs[3],45); return r;
}
static void seed_rng(uint64_t s){
    for(int i=0;i<4;i++){ s+=0x9E3779B97f4A7C15ULL; uint64_t z=s;
        z=(z^(z>>30))*0xBF58476D1CE4E5B9ULL; z=(z^(z>>27))*0x94D049BB133111EBULL;
        rs[i]=z^(z>>31); }
    for(int i=0;i<64;i++) nextr();
}
static inline double rnd(void){ return (nextr()>>11)*0x1.0p-53; }
static inline uint32_t rndi(uint32_t m){ return (uint32_t)(rnd()*m); }

/* --------------------------------------------------------------- lattice */
static int NL,NP,NS,Lx=0,Ly=0,Lz=0;
static int (*plq)[4];
static int *nbrcnt,(*nbr)[24];
static unsigned char *spin;
static int *px,*py,*pz,*pd,*lidx;

/* Explicit signed Gauss equations are supplied by the named geometry writer.
 * No random draws: check initialization, bounded sweep/rotation/replay
 * checkpoints, and termination. Counts include equilibration and production. */
static int ng,(*gedge)[6],(*gsign)[6],*gdegree,*grhs;
static long gauss_states=0,gauss_equations=0,gauss_errors=0;
static int gauss_max=0;
static int check_gauss(const unsigned char*s){
    gauss_states++;
    for(int v=0;v<ng;v++){
        int r=-grhs[v];
        for(int j=0;j<gdegree[v];j++) r+=gsign[v][j]*(s[gedge[v][j]]?1:-1);
        gauss_equations++;
        if(abs(r)>gauss_max) gauss_max=abs(r);
        if(r) gauss_errors++;
    }
    if(gauss_errors) fprintf(stderr,"Gauss violation: states=%ld equations=%ld errors=%ld max=%d\n",
                            gauss_states,gauss_equations,gauss_errors,gauss_max);
    return gauss_errors==0;
}

static inline int flippable(const unsigned char*s,int f){
    const int*P=plq[f];
    int a=s[P[0]],b=s[P[1]],c=s[P[2]],d=s[P[3]];
    return (a==b)&&(c==d)&&(a!=c);
}
static inline void doflip(unsigned char*s,int f){
    const int*P=plq[f]; s[P[0]]^=1; s[P[1]]^=1; s[P[2]]^=1; s[P[3]]^=1;
}
static int totflip(const unsigned char*s){ int t=0; for(int f=0;f<NP;f++) t+=flippable(s,f); return t; }

/* ------------------------------------------------------------ SSE state */
static int M,n;
static unsigned char *otype;
static int *oplq,*lastpos,*nblock;

static void grow(int newM){
    unsigned char*t=(unsigned char*)calloc(newM,1);
    int*q=(int*)calloc(newM,sizeof(int));
    int j=0; for(int p=0;p<M;p++) if(otype[p]){ t[j]=otype[p]; q[j]=oplq[p]; j++; }
    free(otype); free(oplq); otype=t; oplq=q; M=newM;
}

static long nswitch=0,nswtry=0,nillegal=0;

static void sweep(double beta,double lam,double Cd){
    const double pins=beta*NP*Cd;
    for(int f=0;f<NP;f++){ lastpos[f]=-1; nblock[f]=0; }
    for(int p=0;p<M;p++){
        int t=otype[p];
        if(t==0){
            double acc=pins/(double)(M-n);
            if(acc>=1.0||rnd()<acc){ otype[p]=1; oplq[p]=(int)rndi(NP); n++; }
            else continue;
        } else if(t==1){
            double acc=(double)(M-n+1)/pins;
            if(acc>=1.0||rnd()<acc){ otype[p]=0; n--; continue; }
        }
        int f=oplq[p], pp=lastpos[f];
        int told=otype[p];      /* the state must be propagated with the OLD type:
                                   the pair switch preserves the net action on [pp,p] */
        if(pp>=0 && nblock[f]==0){
            nswtry++;
            int tA=otype[pp],tB=otype[p],fl=flippable(spin,f);
            int ok; double ratio;
            if(tA==1&&tB==1){ ok=fl; ratio=(lam/Cd)*(lam/Cd); }
            else if(tA==2&&tB==2){ ok=1; ratio=(Cd/lam)*(Cd/lam); }
            else { ok=fl; ratio=1.0; }
            if(ok&&(ratio>=1.0||rnd()<ratio)){
                int nA=3-tA,nB=3-tB;
                int delta=(nA==2)?+1:-1;
                for(int a=0;a<nbrcnt[f];a++){ int g=nbr[f][a];
                    if(lastpos[g]>=0&&lastpos[g]<pp) nblock[g]+=delta; }
                otype[pp]=nA; otype[p]=nB; nswitch++;
            }
        }
        if(told==2){ if(!flippable(spin,f)) nillegal++; doflip(spin,f); }
        if(otype[p]==2)
            for(int a=0;a<nbrcnt[f];a++){ int g=nbr[f][a]; if(lastpos[g]>=0) nblock[g]++; }
        lastpos[f]=p; nblock[f]=0;
    }
}

/* ---------------------------------------------------------- measurement */
#define NTAU 21
#define NT0  24
#define MAXK 16
static double *tt;
static signed char *A1,*A2;
static short *A3;
static inline int locate(double t,int nn){
    int lo=0,hi=nn; while(lo<hi){ int mid=(lo+hi)>>1; if(tt[mid]<=t) lo=mid+1; else hi=mid; }
    return lo;
}

int main(int argc,char**argv){
    if(argc<9){ fprintf(stderr,"usage: sse geo beta lam C neq nmeas seed nbin [tag]\n"); return 1; }
    double beta=atof(argv[2]),lam=atof(argv[3]),Cd=atof(argv[4]);
    long neq=atol(argv[5]),nme=atol(argv[6]);
    uint64_t seed=strtoull(argv[7],NULL,10);
    int nbin=atoi(argv[8]);
    const char*tag=(argc>9)?argv[9]:"run";

    FILE*fh=fopen(argv[1],"r"); if(!fh){ perror(argv[1]); return 1; }
    if(fscanf(fh,"%d %d",&NL,&NP)!=2) return 1;
    plq=malloc(sizeof(int)*4*NP);
    for(int f=0;f<NP;f++) if(fscanf(fh,"%d %d %d %d",&plq[f][0],&plq[f][1],&plq[f][2],&plq[f][3])!=4) return 1;
    spin=calloc(NL,1);
    for(int j=0;j<NL;j++){ int b; if(fscanf(fh,"%d",&b)!=1) return 1; if(b!=0&&b!=1)return 2; spin[j]=(unsigned char)b; }
    px=malloc(sizeof(int)*NL); py=malloc(sizeof(int)*NL);
    pz=malloc(sizeof(int)*NL); pd=malloc(sizeof(int)*NL);
    for(int j=0;j<NL;j++){ if(fscanf(fh,"%d %d %d %d",&px[j],&py[j],&pz[j],&pd[j])!=4) return 1;
        if(px[j]+1>Lx)Lx=px[j]+1; if(py[j]+1>Ly)Ly=py[j]+1; if(pz[j]+1>Lz)Lz=pz[j]+1; }
    if(fscanf(fh,"%d",&ng)!=1||ng<1) return 2;
    gedge=malloc(sizeof(int)*6*ng); gsign=malloc(sizeof(int)*6*ng);
    gdegree=malloc(sizeof(int)*ng); grhs=malloc(sizeof(int)*ng);
    for(int v=0;v<ng;v++){
        if(fscanf(fh,"%d %d",&grhs[v],&gdegree[v])!=2||gdegree[v]<1||gdegree[v]>6) return 2;
        for(int j=0;j<gdegree[v];j++)
            if(fscanf(fh,"%d %d",&gedge[v][j],&gsign[v][j])!=2 ||
               gedge[v][j]<0||gedge[v][j]>=NL||abs(gsign[v][j])!=1) return 2;
    }
    fclose(fh);
    if(!check_gauss(spin)) return 20;
    NS=Lx*Ly*Lz;
    lidx=malloc(sizeof(int)*NS*3);
    for(int i=0;i<NS*3;i++) lidx[i]=-1;
    for(int e=0;e<NL;e++){ int v=(px[e]*Ly+py[e])*Lz+pz[e]; lidx[v*3+pd[e]]=e; }

    nbrcnt=calloc(NP,sizeof(int)); nbr=malloc(sizeof(int)*24*NP);
    { int*cnt=calloc(NL,sizeof(int)); int(*lp)[8]=malloc(sizeof(int)*8*NL);
      for(int f=0;f<NP;f++) for(int a=0;a<4;a++){ int e=plq[f][a]; int dup=0;
          for(int b=0;b<cnt[e];b++) if(lp[e][b]==f) dup=1;
          if(!dup&&cnt[e]<8) lp[e][cnt[e]++]=f; }
      for(int f=0;f<NP;f++) for(int a=0;a<4;a++){ int e=plq[f][a];
          for(int b=0;b<cnt[e];b++){ int g=lp[e][b]; if(g==f) continue; int dup=0;
              for(int c=0;c<nbrcnt[f];c++) if(nbr[f][c]==g) dup=1;
              if(!dup&&nbrcnt[f]<24) nbr[f][nbrcnt[f]++]=g; } }
      free(cnt); free(lp); }

    seed_rng(seed);
    M=64; n=0; otype=calloc(M,1); oplq=calloc(M,sizeof(int));
    lastpos=malloc(sizeof(int)*NP); nblock=malloc(sizeof(int)*NP);
    unsigned char*sp=malloc(NL),*s0=malloc(NL);
    unsigned char*tb=NULL; int*qb=NULL; int tbsz=0;
    long closure_err=0;
    long guard_stride=(neq+nme+15)/16; if(guard_stride<1)guard_stride=1;

    for(long s=0;s<neq;s++){
        memcpy(s0,spin,NL);
        sweep(beta,lam,Cd);
        if(memcmp(s0,spin,NL)) closure_err++;
        if((s%guard_stride==0||s+1==neq)&&!check_gauss(spin))return 20;
        if(n*1.35+16>M) grow((int)(n*1.35)+16);
        int r=(int)rndi(M);
        if(r){
            if(tbsz<M){ free(tb); free(qb); tb=malloc(M); qb=malloc(sizeof(int)*M); tbsz=M; }
            memcpy(sp,spin,NL);
            for(int p=0;p<r;p++) if(otype[p]==2) doflip(sp,oplq[p]);
            for(int p=0;p<M;p++){ int u=p+r; if(u>=M)u-=M; tb[p]=otype[u]; qb[p]=oplq[u]; }
            memcpy(otype,tb,M); memcpy(oplq,qb,sizeof(int)*M); memcpy(spin,sp,NL);
        }
        if((s%guard_stride==0||s+1==neq)&&!check_gauss(spin))return 20;
    }
    fprintf(stderr,"[%s] equilibrated: M=%d n=%d closure_err=%ld illegal=%ld switch_acc=%.4f\n",
            tag,M,n,closure_err,nillegal,(double)nswitch/(nswtry?nswtry:1));

    int nmax=M+8;
    tt=malloc(sizeof(double)*(nmax+2));
    A1=malloc(nmax+2); A2=malloc(nmax+2); A3=malloc(sizeof(short)*(nmax+2));
    if(tbsz<M){ free(tb); free(qb); tb=malloc(M); qb=malloc(sizeof(int)*M); tbsz=M; }

    int kx[MAXK],ky[MAXK],kz[MAXK],nk=0;
    if(NS>1){
        int cand[12][3]={{0,0,0},{1,0,0},{0,0,1},{1,1,0},{1,1,1},{2,0,0},{2,2,0},
                         {2,2,2},{2,0,1},{1,2,2},{0,2,2},{3,0,0}};
        for(int i=0;i<12;i++) if(cand[i][0]<Lx&&cand[i][1]<Ly&&cand[i][2]<Lz&&nk<MAXK){
            kx[nk]=cand[i][0]; ky[nk]=cand[i][1]; kz[nk]=cand[i][2]; nk++; }
    }
    double *cph=malloc(sizeof(double)*(nk?nk:1)*NS),*sph=malloc(sizeof(double)*(nk?nk:1)*NS);
    for(int a=0;a<nk;a++) for(int x=0;x<Lx;x++) for(int y=0;y<Ly;y++) for(int z=0;z<Lz;z++){
        int v=(x*Ly+y)*Lz+z;
        double ph=2*M_PI*((double)kx[a]*x/Lx+(double)ky[a]*y/Ly+(double)kz[a]*z/Lz);
        cph[a*NS+v]=cos(ph); sph[a*NS+v]=sin(ph); }
    int RMAX=(Lz>1)?Lz:1;

    long meas_per_bin=nme/nbin; if(meas_per_bin<1) meas_per_bin=1;
    double taus[NTAU]; for(int i=0;i<NTAU;i++) taus[i]=0.5*beta*i/(NTAU-1);

    char fn[512]; snprintf(fn,sizeof fn,"%s.bins",tag);
    FILE*fo=fopen(fn,"w");
    fprintf(fo,"# NL %d NP %d beta %g lam %g C %g M %d seed %llu nbin %d NTAU %d nk %d RMAX %d\n",
            NL,NP,beta,lam,Cd,M,(unsigned long long)seed,nbin,NTAU,nk,RMAX);
    fprintf(fo,"# taus:"); for(int i=0;i<NTAU;i++) fprintf(fo," %g",taus[i]); fprintf(fo,"\n");
    fprintf(fo,"# kpts:"); for(int a=0;a<nk;a++) fprintf(fo," %d,%d,%d",kx[a],ky[a],kz[a]); fprintf(fo,"\n");
    char fn2[512]; snprintf(fn2,sizeof fn2,"%s.nseries",tag);
    FILE*fs=(argc>10)?fopen(fn2,"w"):NULL;   /* n-series dump behind a flag; draws no random number */

    double an=0,an2=0,asq=0,afl=0;
    double G1[NTAU],G2[NTAU],G3[NTAU]; for(int i=0;i<NTAU;i++)G1[i]=G2[i]=G3[i]=0;
    double *Sk=calloc(nk?nk:1,sizeof(double));
    double *Cpar=calloc(RMAX,sizeof(double)),*Cperp=calloc(RMAX,sizeof(double));
    double *Cnn=calloc(RMAX,sizeof(double)); double nn1=0,aflloc=0;
    long cnt=0,bins_done=0;
    nswitch=nswtry=0; /* Keep cumulative warmup invariant failures. */

    for(long s=0;s<nme;s++){
        memcpy(s0,spin,NL);
        sweep(beta,lam,Cd);
        if(memcmp(s0,spin,NL)) closure_err++;
        if((s%guard_stride==0||s+1==nme)&&!check_gauss(spin))return 20;
        int r=(int)rndi(M);
        if(r){
            memcpy(sp,spin,NL);
            for(int p=0;p<r;p++) if(otype[p]==2) doflip(sp,oplq[p]);
            for(int p=0;p<M;p++){ int u=p+r; if(u>=M)u-=M; tb[p]=otype[u]; qb[p]=oplq[u]; }
            memcpy(otype,tb,M); memcpy(oplq,qb,sizeof(int)*M); memcpy(spin,sp,NL);
        }
        if((s%guard_stride==0||s+1==nme)&&!check_gauss(spin))return 20;
        int n2=0; for(int p=0;p<M;p++) if(otype[p]==2) n2++;
        an+=n; an2+=n2; asq+=(double)n*(double)n;
        if(fs) fprintf(fs,"%d %d\n",n,n2);

        memcpy(sp,spin,NL);
        int j=0; double flsum=0,fl1=0; int tf=totflip(sp);
        int psample=(n>0)?(int)rndi(n):0;
        for(int p=0;p<M;p++){
            if(!otype[p]) continue;
            A1[j]=(signed char)flippable(sp,0);
            A2[j]=(signed char)(sp[0]?1:-1);
            A3[j]=(short)tf; flsum+=tf; fl1+=A1[j];
            if(j==psample&&nk>0){
                for(int a=0;a<nk;a++){
                    double sr[3]={0,0,0},si[3]={0,0,0};
                    for(int e=0;e<NL;e++){
                        int v=(px[e]*Ly+py[e])*Lz+pz[e];
                        double ev=sp[e]?0.5:-0.5;
                        sr[pd[e]]+=ev*cph[a*NS+v]; si[pd[e]]+=ev*sph[a*NS+v]; }
                    double tr=0; for(int d=0;d<3;d++) tr+=sr[d]*sr[d]+si[d]*si[d];
                    Sk[a]+=tr/NS; }
                for(int rr=0;rr<RMAX;rr++){
                    double cp=0,cq=0; int m=0;
                    for(int x=0;x<Lx;x++)for(int y=0;y<Ly;y++)for(int z=0;z<Lz;z++){
                        int e1=lidx[((x*Ly+y)*Lz+z)*3+2];
                        int e2=lidx[((x*Ly+y)*Lz+(z+rr)%Lz)*3+2];
                        int e3=lidx[((((x+rr)%Lx)*Ly+y)*Lz+z)*3+2];
                        if(e1<0||e2<0||e3<0) continue;
                        cp+=(sp[e1]?0.5:-0.5)*(sp[e2]?0.5:-0.5);
                        cq+=(sp[e1]?0.5:-0.5)*(sp[e3]?0.5:-0.5); m++; }
                    if(m){ Cpar[rr]+=cp/m; Cperp[rr]+=cq/m; } }
                for(int rr=0;rr<RMAX;rr++){
                    double c=0; int m=0;
                    for(int site=0;site<NS;site++){
                        int z=site%Lz,y=(site/Lz)%Ly,x=site/(Lz*Ly);
                        int site2=(x*Ly+y)*Lz+((z+rr)%Lz);
                        c+=flippable(sp,3*site)*flippable(sp,3*site2); m++; }
                    if(m) Cnn[rr]+=c/m; }
                nn1+=1.0;
            }
            if(otype[p]==2){
                int f=oplq[p];
                tf-=flippable(sp,f); for(int a=0;a<nbrcnt[f];a++) tf-=flippable(sp,nbr[f][a]);
                doflip(sp,f);
                tf+=flippable(sp,f); for(int a=0;a<nbrcnt[f];a++) tf+=flippable(sp,nbr[f][a]);
            }
            j++;
        }
        if(memcmp(sp,spin,NL)) closure_err++;
        if((s%guard_stride==0||s+1==nme)&&!check_gauss(sp))return 20;
        if(n>0){ afl+=flsum/n; aflloc+=fl1/n; }

        if(n>1){
            double acc=0;
            for(int i=0;i<n;i++){ acc+=-log(1.0-rnd()); tt[i]=acc; }
            double tot=acc+(-log(1.0-rnd()));
            double sc=beta/tot; for(int i=0;i<n;i++) tt[i]*=sc;
            for(int q=0;q<NT0;q++){
                double u=rnd()*beta; int i0=locate(u,n); if(i0>=n) i0-=n;
                for(int i=0;i<NTAU;i++){
                    double v=u+taus[i]; if(v>=beta) v-=beta;
                    int i1=locate(v,n); if(i1>=n) i1-=n;
                    G1[i]+=(double)A1[i0]*A1[i1];
                    G2[i]+=(double)A2[i0]*A2[i1]*0.25;
                    G3[i]+=(double)A3[i0]*A3[i1];
                }
            }
        }
        cnt++;
        if(cnt==meas_per_bin&&bins_done<nbin){
            double c=(double)cnt,ct=c*NT0;
            fprintf(fo,"%.10g %.10g %.10g %.10g %.10g",an/c,an2/c,asq/c,afl/c,aflloc/c);
            for(int i=0;i<NTAU;i++) fprintf(fo," %.10g",G1[i]/ct);
            for(int i=0;i<NTAU;i++) fprintf(fo," %.10g",G2[i]/ct);
            for(int i=0;i<NTAU;i++) fprintf(fo," %.10g",G3[i]/ct);
            for(int a=0;a<nk;a++) fprintf(fo," %.10g",(nn1>0)?Sk[a]/nn1:0.0);
            for(int rr=0;rr<RMAX;rr++) fprintf(fo," %.10g",(nn1>0)?Cpar[rr]/nn1:0.0);
            for(int rr=0;rr<RMAX;rr++) fprintf(fo," %.10g",(nn1>0)?Cperp[rr]/nn1:0.0);
            for(int rr=0;rr<RMAX;rr++) fprintf(fo," %.10g",(nn1>0)?Cnn[rr]/nn1:0.0);
            fprintf(fo,"\n"); fflush(fo);
            an=an2=asq=afl=aflloc=0; nn1=0;
            for(int i=0;i<NTAU;i++)G1[i]=G2[i]=G3[i]=0;
            for(int a=0;a<nk;a++)Sk[a]=0;
            for(int rr=0;rr<RMAX;rr++){Cpar[rr]=Cperp[rr]=Cnn[rr]=0;}
            cnt=0; bins_done++;
        }
    }
    fclose(fo); if(fs) fclose(fs);
    if(!check_gauss(spin))return 20;
    fprintf(stderr,"[%s] done M=%d n=%d closure_err=%ld illegal=%ld switch_acc=%.4f gauss_states=%ld gauss_equations=%ld gauss_errors=%ld gauss_max=%d guard_stride=%ld\n",
            tag,M,n,closure_err,nillegal,(double)nswitch/(nswtry?nswtry:1),
            gauss_states,gauss_equations,gauss_errors,gauss_max,guard_stride);
    return (closure_err||nillegal||gauss_errors)?20:0;
}
"""


# ============================================ geometry: the torus and the ladder
#
# Both geometries carry one bit per link, bit j of the state integer holding
# e_j = 2 E_j in {-1, +1}, and one four-link face tuple (p, q, u, w) per
# plaquette ordered so that W_f raises p and q and lowers u and w.  P_f is
# applicable on a state iff b_p = b_q, b_u = b_w and b_p != b_u.


class Torus:
    """L^3 periodic torus; links owned by their tail site, ordered (site, dir)."""

    def __init__(self, L):
        self.L = L
        self.sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
        self.li = {}
        self.pos = []
        self.dir = []
        for s in self.sites:
            for d in range(3):
                self.li[(s, d)] = len(self.pos)
                self.pos.append(s)
                self.dir.append(d)
        self.NL = len(self.pos)
        self.inc = {s: [] for s in self.sites}
        for (s, d), j in self.li.items():
            self.inc[s].append((j, +1))
            self.inc[self.step(s, d)].append((j, -1))
        self.plaq = []
        for s in self.sites:
            for d1 in range(3):
                for d2 in range(d1 + 1, 3):
                    a, b = self.step(s, d1), self.step(s, d2)
                    self.plaq.append(
                        (self.li[(s, d1)], self.li[(a, d2)], self.li[(b, d1)], self.li[(s, d2)])
                    )
        self.NP = len(self.plaq)

    def step(self, s, d):
        v = list(s)
        v[d] = (v[d] + 1) % self.L
        return tuple(v)

    def ice(self):
        """The analytic Gauss-law-zero configuration, declared not searched:
        e(v,x) = (-1)^{v_y+v_z}, e(v,y) = (-1)^{v_z+v_x}, e(v,z) = (-1)^{v_x+v_y}."""
        bits = 0
        for (s, d), j in self.li.items():
            other = sum(s[i] for i in range(3) if i != d)
            if other % 2 == 0:
                bits |= 1 << j
        return bits

    def gauss_residual_one(self, bits):
        """max_v |2 (div E)_v| for one configuration, at rho = 0."""
        r = 0
        for s, lst in self.inc.items():
            tot = sum(sg * (1 if (bits >> j) & 1 else -1) for j, sg in lst)
            r = max(r, abs(tot))
        return r


def torus_sector(lat, cap=1 << 18):
    """Gauss sector at rho = 0 by a slab sweep; returns the sorted basis and the peak."""
    order = sorted(lat.sites, key=lambda s: (s[2], s[1], s[0]))
    seen, todo = set(), []
    for s in order:
        new = [j for (j, _) in lat.inc[s] if j not in seen]
        seen.update(new)
        todo.append(new)
    part = np.zeros(1, dtype=np.int64)
    peak = 1
    for k, s in enumerate(order):
        new = todo[k]
        if new:
            offs = np.array(
                [
                    sum(1 << new[a] for a in range(len(new)) if (mm >> a) & 1)
                    for mm in range(1 << len(new))
                ],
                dtype=np.int64,
            )
            cand = (part[:, None] | offs[None, :]).ravel()
        else:
            cand = part
        tot = np.zeros(cand.size, dtype=np.int64)
        for (j, sg) in lat.inc[s]:
            tot += sg * (2 * ((cand >> j) & 1) - 1)
        part = cand[tot == 0]
        peak = max(peak, part.size)
        if peak > cap:
            raise MemoryError(peak)
    return np.unique(part), peak


# ---- the ladder: T_i = 3i (top rail), B_i = 3i+1 (bottom rail), R_i = 3i+2 (rung)


def ladder_plaq(L):
    """f_i : t_i -> t_{i+1} -> b_{i+1} -> b_i, so W_{f_i} raises T_i, R_i and
    lowers R_{i+1}, B_i.  Ordered (p, q, u, w) = (T_i, R_i, R_{i+1}, B_i)."""
    return [(3 * i, 3 * i + 2, 3 * ((i + 1) % L) + 2, 3 * i + 1) for i in range(L)]


def ladder_background(L):
    """2 rho(t_i) = (-1)^i, 2 rho(b_i) = -(-1)^i: odd at z = 3, and neutral."""
    return [(-1) ** i for i in range(L)], [-((-1) ** i) for i in range(L)]


def ladder_sector(L, rt, rb):
    """Every e-config with G_v = 0 at every vertex, as a sorted int64 array.

    At t_i:  e_T[i] - e_T[i-1] - e_R[i] = 2 rho(t_i)
    At b_i:  e_B[i] - e_B[i-1] + e_R[i] = 2 rho(b_i)
    Column transfer; the boundary datum is (e_T[L-1], e_B[L-1])."""
    out = []
    for eT0 in (-1, 1):
        for eB0 in (-1, 1):
            S = np.zeros(1, dtype=np.int64)
            pT = np.full(1, eT0, dtype=np.int64)
            pB = np.full(1, eB0, dtype=np.int64)
            for i in range(L):
                nS, nT, nB = [], [], []
                for eR in (-1, 1):
                    eT = rt[i] + pT + eR
                    eB = rb[i] + pB - eR
                    m = (np.abs(eT) == 1) & (np.abs(eB) == 1)
                    if not m.any():
                        continue
                    s2 = S[m].copy()
                    s2 |= (eT[m] == 1).astype(np.int64) << (3 * i)
                    s2 |= (eB[m] == 1).astype(np.int64) << (3 * i + 1)
                    if eR == 1:
                        s2 |= np.int64(1) << (3 * i + 2)
                    nS.append(s2)
                    nT.append(eT[m])
                    nB.append(eB[m])
                if not nS:
                    S = np.zeros(0, dtype=np.int64)
                    break
                S = np.concatenate(nS)
                pT = np.concatenate(nT)
                pB = np.concatenate(nB)
            if S.size:
                keep = (pT == eT0) & (pB == eB0)
                out.append(S[keep])
    return np.unique(np.concatenate(out)) if out else np.zeros(0, dtype=np.int64)


def ladder_gauss_residual(L, S, rt, rb):
    """max |G_v| over every state and vertex, re-derived from the listed bits."""
    j = np.arange(3 * L)
    e = (2 * ((S[:, None] >> j[None, :]) & 1) - 1).astype(np.int64)
    eT, eB, eR = e[:, 0::3], e[:, 1::3], e[:, 2::3]
    r = 0
    for i in range(L):
        im = (i - 1) % L
        r = max(r, int(np.abs(eT[:, i] - eT[:, im] - eR[:, i] - rt[i]).max()))
        r = max(r, int(np.abs(eB[:, i] - eB[:, im] + eR[:, i] - rb[i]).max()))
    return r


# ------------------------------------------- the plaquette-flip graph and H


def flip_edges(plaq, S):
    """Undirected edges of the plaquette-flip graph on the sorted basis S.

    Only the raising direction is enumerated, so every undirected edge appears
    exactly once.  Returns (a, b, f) as three int arrays."""
    A, B, F = [], [], []
    for f, (p, q, u, w) in enumerate(plaq):
        m = (
            (((S >> p) & 1) == 0)
            & (((S >> q) & 1) == 0)
            & (((S >> u) & 1) == 1)
            & (((S >> w) & 1) == 1)
        )
        if not m.any():
            continue
        tgt = (S[m] | (np.int64(1) << p) | (np.int64(1) << q)) & ~(
            (np.int64(1) << u) | (np.int64(1) << w)
        )
        a = np.nonzero(m)[0]
        b = np.searchsorted(S, tgt)
        A.append(a)
        B.append(b)
        F.append(np.full(a.size, f))
    if not A:
        z = np.zeros(0, dtype=np.int64)
        return z, z, z
    return np.concatenate(A), np.concatenate(B), np.concatenate(F)


def build_H(plaq, S, lam=LAM):
    """-lambda sum_f P_f in the Gauss basis: every off-diagonal entry -lambda."""
    a, b, _ = flip_edges(plaq, S)
    n = S.size
    rows = np.concatenate([a, b])
    cols = np.concatenate([b, a])
    vals = np.full(rows.size, -lam)
    if rows.size == 0:
        return sp.csr_matrix((n, n))
    return sp.coo_matrix((vals, (rows, cols)), shape=(n, n)).tocsr()


def components_of(plaq, S):
    """Connected components of the plaquette-flip graph, as a label array."""
    a, b, _ = flip_edges(plaq, S)
    n = S.size
    G = sp.coo_matrix((np.ones(a.size), (a, b)), shape=(n, n))
    ncomp, lab = connected_components(G, directed=False)
    return ncomp, lab


def cycle_parity_census(a, b, f, n, mode):
    """Spanning tree + fundamental cycles of the plaquette-flip graph.

    Each edge carries the plaquette it flips.  A closed walk's PLAQUETTE PARITY
    is the sum mod 2, per plaquette, of the flips it performs -- a vector over
    GF(2).  The tree is grown from node 0 with every adjacency list in the
    canonical order (face index, then endpoint index), so `odd` -- the number
    of fundamental cycles of non-zero parity -- is reproducible from that rule.
    It is nevertheless a property of the tree; `rank`, the dimension of the
    image of the whole cycle space, is what no tree choice can change."""
    ne = a.size
    adj = [[] for _ in range(n)]
    order_e = sorted(range(ne), key=lambda ei: (int(f[ei]), int(a[ei]), int(b[ei])))
    for ei in order_e:
        adj[int(a[ei])].append((int(b[ei]), ei))
        adj[int(b[ei])].append((int(a[ei]), ei))
    for x in range(n):
        adj[x].sort(key=lambda t: (int(f[t[1]]), t[0]))
    par = [None] * n
    pare = [None] * n
    seen = [False] * n
    tree = [False] * ne
    order = []
    if mode == "bfs":
        dq = deque([0])
        seen[0] = True
        while dq:
            x = dq.popleft()
            order.append(x)
            for y, ei in adj[x]:
                if not seen[y]:
                    seen[y] = True
                    par[y], pare[y], tree[ei] = x, ei, True
                    dq.append(y)
    else:
        stk = [0]
        seen[0] = True
        while stk:
            x = stk.pop()
            order.append(x)
            for y, ei in adj[x]:
                if not seen[y]:
                    seen[y] = True
                    par[y], pare[y], tree[ei] = x, ei, True
                    stk.append(y)
    if not all(seen):
        raise RuntimeError("graph not connected")
    rootpar = [0] * n
    for x in order:
        if par[x] is not None:
            rootpar[x] = rootpar[par[x]] ^ (1 << int(f[pare[x]]))
    ncyc = odd = 0
    basis = []
    for ei in range(ne):
        if tree[ei]:
            continue
        ncyc += 1
        p = rootpar[int(a[ei])] ^ rootpar[int(b[ei])] ^ (1 << int(f[ei]))
        if p:
            odd += 1
        x = p
        for bb in basis:
            x = min(x, x ^ bb)
        if x:
            basis.append(x)
            basis.sort(reverse=True)
    return ne, ncyc, odd, len(basis)


def write_geo(lat_plaq, NL, init_bits, pos, dirs, path):
    """The engine's geometry file: sizes, the face tuples, the initial bits, the
    tail site and direction of every link."""
    with open(path, "w") as fh:
        fh.write(f"{NL} {len(lat_plaq)}\n")
        for (p, q, u, w) in lat_plaq:
            fh.write(f"{p} {q} {u} {w}\n")
        fh.write(" ".join(str((init_bits >> j) & 1) for j in range(NL)) + "\n")
        for j in range(NL):
            if pos is None:
                fh.write("0 0 0 0\n")
            else:
                x, y, z = pos[j]
                fh.write(f"{x} {y} {z} {dirs[j]}\n")
        if pos is None:
            L = NL // 3
            assert NL == 3 * L and len(lat_plaq) == L
            rt, rb = ladder_background(L)
            equations = []
            for i in range(L):
                im = (i - 1) % L
                equations.extend([
                    (rt[i], [(3*i, 1), (3*im, -1), (3*i+2, -1)]),
                    (rb[i], [(3*i+1, 1), (3*im+1, -1), (3*i+2, 1)]),
                ])
        else:
            lengths = tuple(max(p[d] for p in pos) + 1 for d in range(3))
            incidence = {tuple(p): [] for p in pos}
            for e, (p, d) in enumerate(zip(pos, dirs)):
                q = list(p); q[d] = (q[d] + 1) % lengths[d]
                incidence[tuple(p)].append((e, 1))
                incidence[tuple(q)].append((e, -1))
            equations = [(0, incidence[p]) for p in sorted(incidence)]
        fh.write(f"{len(equations)}\n")
        for rhs, terms in equations:
            fh.write(f"{rhs} {len(terms)} " + " ".join(f"{e} {sign}" for e, sign in terms) + "\n")


def thermal(w, betas):
    """Exact canonical E(beta) from a full spectrum, shifted for stability."""
    out = {}
    for bta in betas:
        e = np.exp(-bta * (w - w[0]))
        out[bta] = float((w * e).sum() / e.sum())
    return out


# ================================ A  the 2x2x2 Gauss sector and its components

print(
    "H = -lambda sum_f P_f on the 2x2x2 torus and the height-1 ladder at L = 8; "
    "E_e = Z^L_e/2, U_e = sigma^+_e; G_v = (div E)_v - rho_v; lambda = 1; seed 20260903"
)

t2 = Torus(2)
S2, peak2 = torus_sector(t2)
res2 = max(t2.gauss_residual_one(int(s)) for s in S2)
check(
    f"A1 [exact] the 2x2x2 torus in the convention of PR #7911: {t2.NL} links, {len(t2.sites)} vertices "
    f"at z_v = 6, {t2.NP} faces; z_v even, so rho_v = 0 is parity-admissible and neutral. dim(Gauss) = "
    f"{S2.size}, by slab sweep at peak {peak2} partial states, every state re-derived against G_v = 0 "
    f"with max |2 (div E)_v| = {res2}",
    t2.NL == 24 and t2.NP == 24 and S2.size == 9600 and res2 == 0,
)

def n_applicable(plaq, bits):
    """Number of faces on which P_f is applicable in one configuration."""
    c = 0
    for (p, q, u, w) in plaq:
        bp, bq, bu, bw = [(bits >> x) & 1 for x in (p, q, u, w)]
        if bp == bq and bu == bw and bp != bu:
            c += 1
    return c


ice_rows = []
ice_ok = True
for L in (2, 4, 6):
    tl = Torus(L)
    bits = tl.ice()
    r = tl.gauss_residual_one(bits)
    nfl = n_applicable(tl.plaq, bits)
    ice_rows.append((L, tl.NP, nfl))
    ice_ok &= (r == 0) and (2 * nfl == tl.NP)

check(
    "A2 [exact] the analytic Gauss-law-zero configuration on any even L^3 torus, declared not searched: "
    "e(v,x) = (-1)^{v_y+v_z}, e(v,y) = (-1)^{v_z+v_x}, e(v,z) = (-1)^{v_x+v_y}. At L = 2, 4, 6 it has "
    "G_v = 0 at every vertex and exactly half the faces applicable: "
    + ", ".join(f"{n}/{NP} at L = {L}" for L, NP, n in ice_rows),
    ice_ok,
)

def winding_label(lat, bits):
    """Integer sum of 2E on the coordinate-zero cut normal to each axis."""
    return tuple(sum(1 if (bits >> j) & 1 else -1
                     for (site, axis), j in lat.li.items() if axis == d and site[d] == 0)
                 for d in range(3))


ncomp2, lab2 = components_of(t2.plaq, S2)
winding2 = [winding_label(t2, int(bits)) for bits in S2]
a_full, b_full, _ = flip_edges(t2.plaq, S2)
winding_preserved = all(winding2[int(a)] == winding2[int(b)] for a,b in zip(a_full,b_full))
component_winding = {}
for i,c in enumerate(lab2):
    component_winding.setdefault(int(c), set()).add(winding2[i])
zero_components = [int((lab2 == c).sum()) for c,labels in component_winding.items()
                   if labels == {(0,0,0)}]
winding_ok = (len(set(winding2)) == 125 and winding_preserved
              and all(len(v)==1 for v in component_winding.values())
              and sorted(zero_components) == [1]*16+[864])
sizes2 = Counter(Counter(lab2.tolist()).values())
multiset = sorted(sizes2.items(), key=lambda kv: -kv[0])
check(
    f"A3 [exact] under single plaquette flips the sector is not one ergodic component but {ncomp2}: the "
    "full size multiset is "
    + ", ".join(f"{sz} x {mult}" for sz, mult in multiset)
    + f", summing to {sum(sz * m for sz, m in multiset)} states in {sum(m for _, m in multiset)} "
    "components. Explicit sum(2E) cut labels give 125 winding classes; zero winding contains "
    "the 864-state component plus 16 frozen singletons, so components and winding classes differ",
    ncomp2 == 937
    and multiset == [(864, 1), (464, 6), (252, 12), (136, 8), (36, 6), (6, 144), (1, 760)]
    and winding_ok,
)

ice2 = t2.ice()
i_ice = int(np.searchsorted(S2, ice2))
c_ice = int(lab2[i_ice])
n_ice = int((lab2 == c_ice).sum())
sel = np.nonzero(lab2 == c_ice)[0]
Sc = S2[sel]
Hc = build_H(t2.plaq, Sc)
wc, vc = low_spectrum(Hc, 2)
Hf = build_H(t2.plaq, S2)
wf, vf = low_spectrum(Hf, 2)
wt_gs = float((vf[sel, 0] ** 2).sum())
check(
    f"A4 [1e-9] the analytic configuration lies in the {n_ice}-state component, and the global ground "
    f"state of the full {S2.size}-state sector lies there too: E_0 = {wf[0]:.10f} on the full sector "
    f"equals E_0 = {wc[0]:.10f} on that component, and the full-sector ground vector carries weight "
    f"{wt_gs:.10f} on it",
    n_ice == 864
    and abs(float(wf[0]) + 9.0267209135) <= 1e-9
    and abs(float(wc[0]) - float(wf[0])) <= 1e-9
    and abs(wt_gs - 1.0) <= 1e-9,
)

d1_full = float(wf[1] - wf[0])
d1_comp = float(wc[1] - wc[0])
wt_ex = float((vf[sel, 1] ** 2).sum())
# Complete finite-component spectra check the full level and its actual winding.
component_spectra = {}
for c in range(ncomp2):
    ix = np.nonzero(lab2 == c)[0]
    component_spectra[c] = np.linalg.eigvalsh(Hf[ix][:,ix].toarray())
all_levels = np.sort(np.concatenate(list(component_spectra.values())))
first_components = [c for c,w in component_spectra.items() if np.min(np.abs(w-all_levels[1])) <= 1e-9]
first_windings = {next(iter(component_winding[c])) for c in first_components}
expected_first_windings = {tuple(sign*2 if d==j else 0 for d in range(3)) for j in range(3) for sign in (-1,1)}
full_level_ok = (abs(all_levels[0]-wf[0]) <= 1e-9 and abs(all_levels[1]-wf[1]) <= 1e-9
                 and len(first_components)==6 and first_windings==expected_first_windings)
check(
    f"A5 [1e-9] the full-sector first excitation Delta_1 = {d1_full:.10f} carries weight {wt_ex:.2e} on "
    f"the ground state's component; all six first-level components have explicit cut winding "
    f"{sorted(first_windings)}. The component's own internal gap is {d1_comp:.10f}; an observable's "
    "decay additionally requires nonzero spectral overlap and ensemble/projection assumptions. These gaps "
    f"differ by {100 * (d1_comp / d1_full - 1):.1f} per cent",
    abs(d1_full - 1.6276099336) <= 1e-9
    and abs(d1_comp - 2.2257853859) <= 1e-9
    and wt_ex <= 1e-12 and full_level_ok,
)


# ============================== B  the pair update's plaquette-parity obstruction

pidx = {tup: i for i, tup in enumerate(t2.plaq)}


def face_at(lat, ss, d1, d2):
    return pidx[
        (
            lat.li[(ss, d1)],
            lat.li[(lat.step(ss, d1), d2)],
            lat.li[(lat.step(ss, d2), d1)],
            lat.li[(ss, d2)],
        )
    ]


cube_ok = True
for s0 in t2.sites:
    faces = []
    for d1 in range(3):
        for d2 in range(d1 + 1, 3):
            d3 = 3 - d1 - d2
            faces.append(face_at(t2, s0, d1, d2))
            faces.append(face_at(t2, t2.step(s0, d3), d1, d2))
    x = 0
    for k in faces:
        for e in t2.plaq[k]:
            x ^= 1 << e
    cube_ok &= (x == 0) and (len(set(faces)) == 6)

check(
    "B1 [exact] geometric cube relation only: each of the 12 edges of "
    "a unit cube lies in exactly two of its six faces, so the six face link-sets XOR to zero at all "
    f"{len(t2.sites)} cubes of the 2x2x2 torus. XOR closure alone does not establish legal intermediate "
    "flips or an acceptance probability; B4 supplies an actual different legal closed word",
    cube_ok,
)

a2, b2, f2 = flip_edges(t2.plaq, Sc)
ne2, ncy2, odd2_dfs, rank2 = cycle_parity_census(a2, b2, f2, Sc.size, "dfs")
_, _, odd2_bfs, rank2b = cycle_parity_census(a2, b2, f2, Sc.size, "bfs")

Lad = 8
rt, rb = ladder_background(Lad)
plq_l = ladder_plaq(Lad)
Sl = ladder_sector(Lad, rt, rb)
res_l = ladder_gauss_residual(Lad, Sl, rt, rb)
ncomp_l, lab_l = components_of(plq_l, Sl)
sizes_l = sorted(Counter(lab_l.tolist()).values(), reverse=True)
big_l = int(np.argmax(np.bincount(lab_l)))
sel_l = np.nonzero(lab_l == big_l)[0]
Slc = Sl[sel_l]
al, bl, fl = flip_edges(plq_l, Slc)
nel, ncyl, oddl_dfs, rankl = cycle_parity_census(al, bl, fl, Slc.size, "dfs")
_, _, oddl_bfs, ranklb = cycle_parity_census(al, bl, fl, Slc.size, "bfs")

check(
    "B2 [exact] the fundamental-cycle census of the configuration graph, trees grown from the starting "
    f"configuration in the canonical adjacency order. Ladder L = 8: {Slc.size} nodes, {nel} edges, "
    f"{ncyl} cycles, {oddl_dfs} of odd plaquette parity under a depth-first tree and {oddl_bfs} under a "
    f"breadth-first one. 2x2x2 torus: {Sc.size}, {ne2}, {ncy2}, and {odd2_dfs} and {odd2_bfs} "
    "respectively -- a majority either way. Node, edge and cycle counts are invariants; the odd counts "
    "are properties of the tree, so B3 states the obstruction without one",
    (Slc.size, nel, ncyl, oddl_dfs, oddl_bfs) == (47, 104, 58, 0, 0)
    and (Sc.size, ne2, ncy2) == (864, 3456, 2593)
    and min(odd2_dfs, odd2_bfs) > ncy2 // 2,
)

check(
    "B3 [exact] the obstruction without a spanning tree: the rank of the plaquette-parity map on the "
    f"whole cycle space is {rankl} on the ladder and {rank2} on the 2x2x2 torus. Rank 0 says EVERY "
    "closed walk on the ladder has even parity at every face, so the restriction is empty there; rank "
    f"{rank2} gives an algebraic index-{2 ** rank2} kernel on the torus. This is neither a Gibbs-weight "
    "fraction nor a mixing certificate, and does not exclude additional implementation or equilibration errors",
    rankl == 0 and rank2 == 10 and rankl == ranklb and rank2 == rank2b,
)

found = None
adjm = {}
for ei in range(a2.size):
    adjm.setdefault(int(a2[ei]), []).append((int(b2[ei]), int(f2[ei])))
    adjm.setdefault(int(b2[ei]), []).append((int(a2[ei]), int(f2[ei])))
start = int(np.searchsorted(Sc, ice2))
dist = {start: (0, None, None)}
dq = deque([start])
while dq and found is None:
    x = dq.popleft()
    for y, ff in adjm.get(x, []):
        if y not in dist:
            dist[y] = (dist[x][0] + 1, x, ff)
            dq.append(y)
for ei in range(a2.size):
    x, y, ff = int(a2[ei]), int(b2[ei]), int(f2[ei])
    if dist[x][1] is None and dist[y][1] is None:
        continue
    par = 1 << ff
    for z in (x, y):
        c = z
        while dist[c][1] is not None:
            par ^= 1 << dist[c][2]
            c = dist[c][1]
    if par:
        found = sorted(i for i in range(t2.NP) if (par >> i) & 1)
        break
def legal_word_trace(lat, start_bits, word):
    bits = start_bits; states = [bits]
    for f in word:
        p,q,u,w = lat.plaq[f]
        bp,bq,bu,bw = [(bits >> e) & 1 for e in (p,q,u,w)]
        if not (bp==bq and bu==bw and bp!=bu):
            return False, states
        bits ^= sum(1 << e for e in (p,q,u,w)); states.append(bits)
        if lat.gauss_residual_one(bits):return False,states
    return bits == start_bits, states


legal_word = [20,23,14,17]
legal_word_ok, legal_states = legal_word_trace(t2, 15798951, legal_word)
legal_word_parity = 0
for f in legal_word:legal_word_parity ^= 1 << f

check(
    "B4 [exact] an odd-parity closed walk exhibited on the 2x2x2 torus, from the analytic configuration: "
    f"its graph parity is {found}; independent replay of the legal word {legal_word} gives states "
    f"{legal_states} and returns to its start with nonzero parity. "
    "A same-plaquette operator-pair switch creates and destroys off-diagonal operators two at a time at "
    "one face, so it changes every face's flip count by 0 or +-2 and can never realise this walk",
    found is not None and len(found) % 2 == 0 and len(found) >= 6
    and legal_word_ok and legal_word_parity != 0 and legal_states[0]==ice2,
)


# ============================== C  the ladder, and the exact thermal references

check(
    f"C1 [exact] the ladder at L = 8 in the convention of PR #7911, z_v = 3 odd with the declared "
    f"staggered background 2 rho(t_i) = (-1)^i, 2 rho(b_i) = -(-1)^i: dim(Gauss) = {Sl.size} = PR "
    f"#7911's Lucas(8) + 2, every state re-derived with max |G_v| = {res_l}; it splits into {ncomp_l} "
    f"components of sizes {sizes_l}, the dynamical one carrying {Slc.size} states",
    Sl.size == 49 and res_l == 0 and ncomp_l == 3 and sizes_l == [47, 1, 1],
)

Hl = build_H(plq_l, Slc)
wl = np.linalg.eigvalsh(Hl.toarray())
dens = float(wl[0]) / Lad
check(
    f"C2 [1e-9] on that component E_0 = {wl[0]:.10f}, reproducing PR #7911's L = 8 value to the digit, "
    f"with internal gap {wl[1] - wl[0]:.10f} and <P_f> = -E_0/(lambda L) = {-dens:.10f}. The exact L = 8 "
    f"density E_0/L is {dens:.8f} lambda (total energy multiplies by L); the historical -0.6035607 "
    "comparison is a rounded L20 value, not an established infinite-size limit",
    abs(float(wl[0]) + 4.8309586723) <= 1e-9 and abs(dens + 0.6038698340) <= 1e-9,
)

BETAS = (2.0, 4.0, 8.0, 16.0)
th_l = thermal(wl, BETAS)
ref_l = {2.0: -4.5151826280, 4.0: -4.8053520382, 8.0: -4.8305435458, 16.0: -4.8309585028}
check(
    "C3 [1e-9] the exact canonical energy on the 47-state ladder component, the reference the witness "
    "rows are held to: E(beta) = "
    + ", ".join(f"{th_l[bt]:.10f} at beta = {bt:g}" for bt in BETAS),
    all(abs(th_l[bt] - ref_l[bt]) <= 1e-9 for bt in BETAS),
)

wc_full, component_vectors = np.linalg.eigh(Hc.toarray())
# An actual transverse observable can miss the component's lowest excitation.
transverse = np.array([sum(((-1)**site[0]) * (1 if (int(bits)>>j)&1 else -1) / 2
                          for (site,d),j in t2.li.items() if d==1) / math.sqrt(len(t2.sites))
                       for bits in Sc])
transverse_weights = np.abs(component_vectors.T @ (transverse*component_vectors[:,0]))**2
observable_indices = np.nonzero((wc_full-wc_full[0] > 1e-9) & (transverse_weights > 1e-12))[0]
transverse_gap = float(wc_full[int(observable_indices[0])]-wc_full[0])
first_level_weight = float(transverse_weights[np.abs(wc_full-wc_full[1]) < 1e-9].sum())
th_2 = thermal(wc_full, BETAS)
ref_2 = {2.0: -8.6891572261, 4.0: -9.0239679296, 8.0: -9.0267206703, 16.0: -9.0267209135}
check(
    "C4 [1e-9] the same on the 864-state ice component of the 2x2x2 torus: E(beta) = "
    + ", ".join(f"{th_2[bt]:.10f} at beta = {bt:g}" for bt in BETAS)
    + ". This is the specified 864-component Gibbs reference; convergence of a restricted sampler to it is not assumed",
    all(abs(th_2[bt] - ref_2[bt]) <= 1e-9 for bt in BETAS),
)


# ================================ D  [witness] the SSE rows, at the declared seed


def find_compiler():
    """The first working C compiler on PATH, or None."""
    for cc in (os.environ.get("CC"), "cc", "gcc", "clang"):
        if cc and shutil.which(cc):
            return cc
    return None


def run_engine(exe, geo, beta, C, neq, nmeas, tag, seed=SEED, nbin=40):
    """One SSE run; returns the per-bin table and the engine's own invariants."""
    r = subprocess.run(
        [exe, geo, str(beta), str(LAM), str(C), str(neq), str(nmeas), str(seed), str(nbin), tag],
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    Path(tag + ".stdout").write_text(r.stdout)
    Path(tag + ".stderr").write_text(r.stderr)
    if r.returncode != 0:
        raise RuntimeError(f"required engine exit {r.returncode}: " + r.stderr[-400:])
    hdr = {}
    with open(tag + ".bins") as fh:
        toks = fh.readline().split()
        for i in range(1, len(toks) - 1, 2):
            try:
                hdr[toks[i]] = float(toks[i + 1])
            except ValueError:
                pass
        fh.readline()
        fh.readline()
    d = np.loadtxt(tag + ".bins")
    last = r.stderr.strip().splitlines()[-1]
    inv = dict(
        closure_err=int(last.split("closure_err=")[1].split()[0]),
        illegal=int(last.split("illegal=")[1].split()[0]),
        M=int(last.split("M=")[1].split()[0]),
    )
    diagnostics = [line for line in r.stderr.splitlines() if "equilibrated:" in line or " done " in line]
    if len(diagnostics) != 2 or "equilibrated:" not in diagnostics[0] or " done " not in diagnostics[1]:
        raise RuntimeError("missing or malformed required engine diagnostics")
    for line in diagnostics:
        fields = dict(re.findall(r"(closure_err|illegal)=(\d+)", line))
        if set(fields) != {"closure_err", "illegal"} or any(int(x) for x in fields.values()):
            raise RuntimeError("cumulative equilibration/production invariant failure: " + line)
    for key in ("gauss_states", "gauss_equations", "gauss_errors", "gauss_max", "guard_stride"):
        match = re.search(r"\b" + key + r"=(\d+)\b", last)
        if match is None:
            raise RuntimeError("missing required " + key)
        inv[key] = int(match.group(1))
    if inv["gauss_states"] < 2 or inv["gauss_equations"] < inv["gauss_states"] or inv["guard_stride"] < 1 or inv["gauss_errors"] or inv["gauss_max"]:
        raise RuntimeError("missing or failed Gauss equation checks")
    if d.ndim != 2 or d.shape[0] != nbin or not np.isfinite(d).all():
        raise RuntimeError("missing, malformed or nonfinite required bin table")
    required_header = {"NL", "NP", "beta", "lam", "C", "M", "seed", "nbin", "NTAU", "nk", "RMAX"}
    if not required_header <= hdr.keys() or not all(math.isfinite(hdr[k]) for k in required_header):
        raise RuntimeError("missing or nonfinite required bin header")
    with open(geo) as fh:
        expected_nl, expected_np = map(int, fh.readline().split())
    if (hdr["NL"] != expected_nl or hdr["NP"] != expected_np or hdr["beta"] != beta
            or hdr["lam"] != LAM or hdr["C"] != C or hdr["seed"] != seed
            or hdr["nbin"] != nbin or hdr["NTAU"] != 21 or hdr["M"] != inv["M"]
            or d.shape[1] != 5 + 3*int(hdr["NTAU"]) + int(hdr["nk"]) + 3*int(hdr["RMAX"])):
        raise RuntimeError("required bin table does not match the executed geometry/protocol")
    NP, bta, Cd = int(hdr["NP"]), hdr["beta"], hdr["C"]
    NTAU = int(hdr["NTAU"])
    E = NP * Cd - d[:, 0] / bta
    Pf = d[:, 1] / (NP * bta * LAM)
    GE0 = float(d[:, 5 + NTAU].mean())
    nb = d.shape[0]
    inv.update(
        E=float(E.mean()),
        dE=float(E.std(ddof=1) / math.sqrt(nb)),
        Pf=float(Pf.mean()),
        GE0=GE0,
        nbin=nb,
    )
    return inv


CC = find_compiler()
TMP = tempfile.mkdtemp(prefix="link_qmc_")
EXE = os.path.join(TMP, "sse")
qmc = {}
qmc_reason = ""
if CC is None:
    qmc_reason = "no C compiler on PATH (tried $CC, cc, gcc, clang)"
else:
    src = os.path.join(TMP, "sse.c")
    with open(src, "w") as fh:
        fh.write(SSE_C)
    cp = subprocess.run(
        [CC, "-O2", "-o", EXE, src, "-lm"], capture_output=True, text=True, timeout=120
    )
    if cp.returncode != 0:
        CC = None
        qmc_reason = "the embedded C source did not compile: " + cp.stderr.strip()[-200:]

if CC is not None:
    geo_l = os.path.join(TMP, "lad8.geo")
    geo_t = os.path.join(TMP, "t222.geo")
    geo_4 = os.path.join(TMP, "t444.geo")
    write_geo(plq_l, 3 * Lad, int(Slc[0]), None, None, geo_l)
    write_geo(t2.plaq, t2.NL, ice2, t2.pos, t2.dir, geo_t)
    t4 = Torus(4)
    write_geo(t4.plaq, t4.NL, t4.ice(), t4.pos, t4.dir, geo_4)
    try:
        for bt in BETAS:
            qmc[("lad", bt)] = run_engine(
                EXE, geo_l, bt, 2, 20000, 100000, os.path.join(TMP, f"L{bt:g}")
            )
        qmc[("t222", 8.0)] = run_engine(
            EXE, geo_t, 8.0, 2, 20000, 100000, os.path.join(TMP, "T8")
        )
        for Cd in (1, 4, 8):
            qmc[("C", Cd)] = run_engine(
                EXE, geo_t, 8.0, Cd, 20000, 40000, os.path.join(TMP, f"TC{Cd}")
            )
    except Exception as exc:  # pragma: no cover - engine failure is reported, not hidden
        CC = None
        qmc_reason = f"the engine did not complete: {exc}"

if CC is not None:
    dev_l = {bt: abs(qmc[("lad", bt)]["E"] - th_l[bt]) / qmc[("lad", bt)]["dE"] for bt in BETAS}
    check(
        "D1 [witness, seed 20260903] the sign-free SSE for H = -lambda sum_f P_f, compiled here from the "
        "embedded C source, matches this finite seeded ladder diagnostic at L = 8: with C = 2, 2e4 equilibration and 1e5 "
        "sampling sweeps in 40 bins, E(beta) sits "
        + ", ".join(f"{dev_l[bt]:.2f}" for bt in BETAS)
        + " sigma from the exact C3 values at beta = 2, 4, 8, 16, and <P_f> = "
        + f"{qmc[('lad', 16.0)]['Pf']:.6f} at beta = 16 against the exact 0.6038698",
        all(dev_l[bt] <= 2.0 for bt in BETAS)
        and abs(dev_l[2.0] - 0.17) <= 0.01
        and abs(dev_l[4.0] - 0.28) <= 0.01
        and abs(dev_l[8.0] - 0.33) <= 0.01
        and abs(dev_l[16.0] - 1.12) <= 0.01,
    )

    q8 = qmc[("t222", 8.0)]
    dev8 = abs(q8["E"] - th_2[8.0]) / q8["dE"]
    check(
        "D2 [witness, seed 20260903] the same engine, the same parameters and the same declared seed do "
        f"not validate on the 2x2x2 torus: E(beta = 8) = {q8['E']:.6f}({1e6 * q8['dE']:.0f}) against the "
        f"exact {th_2[8.0]:.10f} of C4, which is {dev8:.1f} bin-standard-error units. The pair-parity "
        "obstruction is exact; this witness does not isolate every possible cause of bias",
        dev8 >= 100 and abs(q8["E"] + 8.118460) <= 2e-6 and abs(q8["dE"] - 0.006703) <= 2e-6,
    )

    cs = [qmc[("C", c)] for c in (1, 4, 8)] + [q8]
    pairs = [
        abs(x["E"] - y["E"]) / math.sqrt(x["dE"] ** 2 + y["dE"] ** 2)
        for i, x in enumerate(cs)
        for y in cs[i + 1 :]
    ]
    check(
        "D3 [witness, seed 20260903] the original finite C comparison: at beta = 8 "
        "the diagonal weight C = 1, 4, 8 (2e4 equilibration, 4e4 sampling sweeps) gives "
        + ", ".join(f"{qmc[('C', c)]['E']:.6f}({1e6 * qmc[('C', c)]['dE']:.0f})" for c in (1, 4, 8))
        + f" against C = 2's {q8['E']:.6f}({1e6 * q8['dE']:.0f}); every pair agrees to "
        f"{max(pairs):.1f} combined bin-standard-error units and every one is far from the exact value. "
        "Common seeds and these bins do not calibrate cross-run independence, autocorrelation, finite-M or equilibration error",
        max(pairs) <= 3.0
        and all(abs(x["E"] - th_2[8.0]) / x["dE"] >= 20 for x in cs),
    )

    ge = {k: v["GE0"] for k, v in qmc.items()}
    inv_ok = all(v["closure_err"] == 0 and v["illegal"] == 0 and v["gauss_errors"] == 0
                 and v["gauss_max"] == 0 and v["gauss_states"] >= 2
                 and v["gauss_equations"] >= v["gauss_states"] for v in qmc.values())
    check(
        "D4 [witness, bounded checks] cumulative warmup/production closure and illegal counters are zero; "
        "the API also requires explicit Gauss equations at initialization, bounded sweep/rotation/replay "
        "checkpoints and termination, with positive counts. These are not per-flip Gauss checks. "
        f"Equal-time G_E(0) = {min(ge.values()):.6f}; only E_e^2=1/4 is tested, "
        "and positive-lag indexing remains unvalidated",
        inv_ok and all(abs(g - 0.25) <= 1e-9 for g in ge.values()),
    )
else:
    for tag in ("D1", "D2", "D3", "D4"):
        check(f"{tag} [required witness, seed 20260903] unavailable: {qmc_reason}; partial exact rows are not complete evidence", False)


# ==================== E  [statement] what a correct three-dimensional sampler needs


def comb(n, k):
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


acc = {}
for L in (2, 4):
    tl = Torus(L)
    ncub = len(tl.sites)
    acc[L] = (LAM / 2.0) ** 6 * ncub / comb(tl.NP, 6)
check(
    "E1 [finite geometric arithmetic] picking six of "
    "the N_p faces and switching all six from diagonal to off-diagonal lands on a cube for only N_s of "
    "the C(N_p, 6) six-subsets, times a putative six-operator ratio (lambda/C)^6. At C = 2 that is "
    f"{acc[2]:.1e} on the 2x2x2 torus (N_p = 24, N_s = 8) and {acc[4]:.1e} at 4^3 (192, 64). "
    "This geometric factor is not legal-loop acceptance or mixing; changed representations remain possible",
    acc[2] > 1e-7 and acc[4] < 1e-10,
)

if CC is not None:
    t_start = time.time()
    inv4 = run_engine(EXE, geo_4, 16.0, 2, 4000, 4000, os.path.join(TMP, "Q4"), nbin=20)
    rate = (time.time() - t_start) / 8000.0
    check(
        "E2 [witness, measured here] cost of this restricted sampler only. One core, 4^3 torus (192 links, 192 "
        f"faces) at beta = 16, C = 2: 8e3 sweeps at string length M = {inv4['M']} run at "
        f"{1e3 * rate:.2f} ms per sweep, so 2e5 sweeps cost about {rate * 2e5:.0f} s, with "
        f"closure_err = {inv4['closure_err']} and illegal = {inv4['illegal']}. No mixing-time, "
        "unwritten-algorithm performance or error-controlled phase-cost estimate follows",
        rate * 2e5 < 600 and inv4["closure_err"] == 0 and inv4["illegal"] == 0,
    )
else:
    check("E2 [required witness, measured here] unavailable: " + qmc_reason, False)

check(
    "E3 [1e-9] the distinction any future claim has to carry: on the 2x2x2 torus the full-sector first "
    f"excitation is {d1_full:.10f} and the ice component's internal gap is {d1_comp:.10f}. Observable "
    "overlap and the component/ensemble/temperature/estimator determine any extracted decay, and "
    f"they differ by {100 * (d1_comp / d1_full - 1):.1f} per cent at the smallest three-dimensional "
    f"torus. Actual E_y(pi,0,0) first couples at {transverse_gap:.10f}, with total first-level "
    f"weight {first_level_weight:.3e}; an observed decay must name its observable and protocol",
    abs(d1_full - 1.6276099336) <= 1e-9
    and abs(d1_comp - 2.2257853859) <= 1e-9
    and d1_comp > d1_full
    and abs(transverse_gap-2.5172790443) <= 1e-9 and first_level_weight < 1e-20,
)

def fixed_z_readout_counterexample():
    # Actual Gauss states joined by plaquette 5, restricted to their two-state span.
    a,b,f = 166,2196,5
    p,q,u,w = t2.plaq[f]
    legal = (((a>>p)&1)==((a>>q)&1) and ((a>>u)&1)==((a>>w)&1)
             and ((a>>p)&1)!=((a>>u)&1))
    if not legal or a ^ sum(1<<e for e in (p,q,u,w)) != b:return False
    if t2.gauss_residual_one(a) or t2.gauss_residual_one(b):return False
    plus = np.array([[.5,.5],[.5,.5]]);minus = np.array([[.5,-.5],[-.5,.5]])
    Pf = np.array([[0.,1.],[1.,0.]])
    return (np.array_equal(np.diag(plus),np.diag(minus))
            and np.trace(plus@Pf)==1 and np.trace(minus@Pf)==-1)


if CC is not None:
    off_pct = abs(qmc[("t222", 8.0)]["E"] - th_2[8.0]) / abs(th_2[8.0]) * 100.0
    off_txt = f"it is {off_pct:.1f} per cent short in |E|"
else:
    off_txt = "the required witness is unavailable, so complete-unit evidence fails"
check(
    "E4 [source/readout scope check] the scope kept: the 4^3 rows of the source computation are a restricted-sub-ensemble "
    "baseline and no phase is read off them. Where this update can be checked against an exact answer "
    "-- the 2x2x2 torus, C4 -- " + off_txt + ", so nothing is claimed here, either way, about whether "
    "the three-dimensional link sector is gapped or gapless",
    source_scope_certificate() and fixed_z_readout_counterexample(),
)

shutil.rmtree(TMP, ignore_errors=True)

print("per_element: checked E_e squared equals 1/4 at equal time; supplied off-diagonal readout is separate.")
print("per_site: checked every enumerated Gauss state and vertex; C checks explicit equations at bounded checkpoints.")
print("per_mode: checked full/component finite spectra; positive-lag code and observable decay extraction are not validated.")
print("per_block: checked finite cycle parity ranks and a legal odd-parity word; algebraic index is not thermal mass.")
print("lattice_wide: checked two finite geometries and the stated analytic even-L seed; no infinite-volume phase or mixing result.")
print("N1 packet limitation: five-route procedural minimum is unmet; only real executed families and open alternatives are recorded.")
print("SUMMARY: 937 flip components and 125 winding classes; finite full/component gaps differ. "
      "The same-face pair switch preserves parity; rank 0/10 does not fix weighted mass or mixing. "
      "Original seeded discrepancies remain diagnostics. No phase or physical Record dynamics is derived; audit is deferred.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
