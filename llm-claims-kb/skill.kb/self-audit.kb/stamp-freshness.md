# Stamp Freshness

Synthesis views (`<name>.claims.md`, any rolled-up `$CATEGORY.md`)
carry `last-updated`. A view whose stamp predates the newest change
in the collection it rolls up is stale-with-a-stamp -- legal, but
only if read as stale. Compare the stamp against
`git log -1 --format=%cs -- <collection>/`; refresh the view or
accept the debt knowingly.
