# PR7315 own arithmetic hygiene: historical recovery

This packet preserves the complete before/after bodies and patch for the three-file nsimplify cleanup at PR7315. It is historical source and process evidence, not scientific acceptance of the old implementations.

The corrected quotient certificate already uses exact arithmetic and omits the former principal-angle and tau-measurement paths. The two other historical runners have no canonical main path. Restoring them would reintroduce science outside the accepted corrected scopes, so this packet preserves their exact revised bodies without activating them. No current science source is overwritten.

All transferred science remains separately tracked. PR7315 closure requires completion of its remaining seven transfers; this packet alone does not justify closure. Formal audit stays deferred.

Decode an ORIGINAL_BODIES.json occurrence with base64 then gzip; verify its recorded SHA256. ORIGINAL_CHANGE_GZIP_BASE64.json preserves the exact original base-to-head diff. Decode its gzip_base64 field with base64 then gzip; verify the recorded uncompressed SHA256. Encoding preserves whitespace in the original patch.
