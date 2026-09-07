# #7840 raw Git ancestry confirmation

**Confirmed:** the unique actual merge base of #7840 head `a664eea7a8d867e1e3ddc3759ce0d26d097e262f` and current main `a8f84aaad75fdcb790ba6ba094e4275e237d9a5a` is **`36fe57a7a784df31bc2178c4b94dfc7caaa5d094`**. This is an exact raw-object result, not an inference from absent shallow history.

The check used the separate bare repository `objects-view.git`, with `objects/info/alternates` pointing to `/Users/jonreilly/Projects/Physics/.git/objects`, no refs or shallow metadata copied, and replacement objects disabled. Git reports `--is-shallow-repository=false`. No fetch/network command, source change or shared repository setting change was performed.

`git merge-base --all` returned that single base without errors, and `--is-ancestor` succeeded for both head and main. The complete head-side segment is:

```text
a664eea7a8d867e1e3ddc3759ce0d26d097e262f
  parent 5cf8a4e5093d1cef2a75caf6240bb5a0a1bcfb13
    parent bfb88f94a3916ea09ca5c0a8752797e3d8b12979
      parent 36fe57a7a784df31bc2178c4b94dfc7caaa5d094
```

The original base-to-head tree delta contains **exactly 18 paths**: the **17 selected inherited source paths**, all additions, and the generated citation manifest. There are no other changed/deleted paths and no selected path missing from this delta. Each selected new blob equals both `parent_blob` and `final_blob` in the light review's `closed_parent_7840` map. Each also matches the actual final tower `2814c6768e4d7b38048f70ad7883b4951cb12da3` blob and the SHA256 in `selected_main_coverage`. The generated manifest is fully recorded as original evidence and remains excluded from source copying; integration regenerates it.

Exact binding:

- #7840 tree: `7fc9156c39f0e69297b33c1c271a08be1ed0f260`.
- Merge-base tree: `f419afe09acbd5aa7846d0a22b2e949570cd59df`.
- Main tree: `f394c1f6033be8acd57d08962491cfcff34c559c`.
- Input map `backlog-light-germ-review/provenance-and-inputs.json` SHA256: `bf3d49d4bd67e58458a449916d7d67cd8fa345de736bde0aaa94897db1ab51bb`.
- Full original delta map SHA256: `f6c89c65ff94ab2080830e0acb5063d020cbb9d6f8d88547a3fde8703683942c`.
- Shared `.git/shallow` before and after SHA256: `dbc04171e6afdffe7410fcb54539147e2b4b236a6e8aa077c3abf3f20e6e4e60` (unchanged; 287 bytes).

`check_ancestry.py`, `commands.json`, `original_delta_map.json`, `shared-shallow-before`, and `receipt.json` preserve the method and machine-readable evidence. No missing-object boundary affected the merge-base or complete original-delta calculation. This does **not** assert that every ancestor/object in the entire repository is present, and it does not change scientific review or applied audit status. The isolated raw-object check resolves only the ancestry caveat for #7840 and its selected original source delta.
