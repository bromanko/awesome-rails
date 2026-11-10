> HISTORICAL REPLAY ONLY: freshness checks the frozen catalog, not current upstream. Outcome labels were held out; live research is not guaranteed blind.

# Freshness research

Advisory only; every suggested change requires maintainer review.
No list edits, PRs, comments, or reviews were submitted.

Catalog revision: `c5fbc8548bccf566f94f7d0c02f7fd80dbf5c847`
Slice: 0 of 142 (zero-based)
Catalog recheck: unchanged

Sources below are agent-reported observations, not independent verification.

## Entry 31

<pre>Rails Official Website

rubyonrails.org is still the official Ruby on Rails website. The entry has no description, and its name and URL are correct.

https://rubyonrails.org
The fetched page is the official Ruby on Rails site. It has the tagline &#x27;Ruby on Rails: Accelerate your agents with convention over configuration&#x27;, lists Rails 8.1.4.1 as the latest release, and links to docs and community resources.

Blocking uncertainties:
None reported.

Informational caveats:
Content was read through a summarizing fetch tool.

Recommendation: keep
Proposed name: None
Proposed URL: None
Proposed description: None</pre>

## Entry 35

<pre>Rails Source Code

github.com/rails/rails is the official, active, unarchived Rails source repository. The reference-style link is correct and needs no change.

https://github.com/rails/rails
The repository description is &#x27;Ruby on Rails&#x27; and it links to rubyonrails.org. It is not archived and shows active development, with about 101k commits and many open issues and PRs.

Blocking uncertainties:
None reported.

Informational caveats:
Content was read through a summarizing fetch tool.

Recommendation: keep
Proposed name: None
Proposed URL: None
Proposed description: None</pre>

## Entry 332

<pre>lobsters

The entry says Rails 7.0, but the pinned official Gemfile.lock (revision 2f385d14) resolves rails 8.1.3.1, so the label should read Rails 8.1. The project is still an active, unarchived Rails link aggregation app that powers lobste.rs, so the description and secondary link stay. The label reflects declared dependencies at that revision, not tested runtime compatibility.

https://github.com/lobsters/lobsters/blob/2f385d149e67f5ff78643dcf6d3cab0b24c0117c/Gemfile.lock
The pinned snapshot lists rails (8.1.3.1), with railties, activerecord and the other framework gems also at 8.1.3.1. &#x27;rails&#x27; appears under DEPENDENCIES.
https://github.com/lobsters/lobsters
The repository is an open-source Rails app for the computing-focused link aggregation and discussion site lobste.rs. It is active and not archived.

Blocking uncertainties:
None reported.

Informational caveats:
The app was not run. The version label reflects the declared lockfile at the pinned revision only, not runtime compatibility or later revisions.
Repository page content was read through a summarizing fetch tool.

Recommendation: update
Proposed name: None
Proposed URL: None
Proposed description: A link aggregation app (using Rails 8.1). - [:earth_africa:](https://lobste.rs)</pre>


# Proposed pull requests

1 proposed change(s); 0 held for unresolved questions.

### Ready for maintainer review
<pre>clear: Search complete (complete=true, no errors). It ran two queries against gramantin/awesome-rails titles, bodies and comments: the name &quot;lobsters&quot; and the URL &quot;https://github.com/lobsters/lobsters&quot;. Neither query returned any records, so there is no open PR, merged change or maintainer rejection about updating the lobsters entry&#x27;s Rails version label from 7.0 to 8.1. This only covers those two queries. Discussions that never mention the project name or URL would not have been found.
{
  &quot;checks&quot;: {
    &quot;apply&quot;: 0,
    &quot;applyCheck&quot;: 0,
    &quot;changedEntryLinks&quot;: 0
  },
  &quot;passed&quot;: true,
  &quot;reason&quot;: &quot;One-entry patch applies; native layout preserved. Changed-entry destinations verified.&quot;,
  &quot;scope&quot;: &quot;Patch applicability, one-entry structure and changed-entry URLs; no upstream lint suite exists in this snapshot.&quot;
}</pre>
<pre>Searches:
repo:gramantin/awesome-rails &quot;lobsters&quot; in:title,body,comments
repo:gramantin/awesome-rails &quot;https://github.com/lobsters/lobsters&quot; in:title,body,comments
References:
</pre>

## entry-332

<pre>Update lobsters entry

The entry says Rails 7.0, but the pinned official Gemfile.lock (revision 2f385d14) resolves rails 8.1.3.1, so the label should read Rails 8.1. The project is still an active, unarchived Rails link aggregation app that powers lobste.rs, so the description and secondary link stay. The label reflects declared dependencies at that revision, not tested runtime compatibility.

Evidence:
https://github.com/lobsters/lobsters/blob/2f385d149e67f5ff78643dcf6d3cab0b24c0117c/Gemfile.lock — The pinned snapshot lists rails (8.1.3.1), with railties, activerecord and the other framework gems also at 8.1.3.1. &#x27;rails&#x27; appears under DEPENDENCIES.
https://github.com/lobsters/lobsters — The repository is an open-source Rails app for the computing-focused link aggregation and discussion site lobste.rs. It is active and not archived.

Informational caveats:
The app was not run. The version label reflects the declared lockfile at the pinned revision only, not runtime compatibility or later revisions.
Repository page content was read through a summarizing fetch tool.

Based on catalog revision c5fbc8548bccf566f94f7d0c02f7fd80dbf5c847.
Proposed by an automated freshness review. A maintainer must verify the evidence and edit.
Validation and discussion checks are recorded below.

Review status: Ready for maintainer review
Prior discussion: clear: Search complete (complete=true, no errors). It ran two queries against gramantin/awesome-rails titles, bodies and comments: the name &quot;lobsters&quot; and the URL &quot;https://github.com/lobsters/lobsters&quot;. Neither query returned any records, so there is no open PR, merged change or maintainer rejection about updating the lobsters entry&#x27;s Rails version label from 7.0 to 8.1. This only covers those two queries. Discussions that never mention the project name or URL would not have been found.
Validation: One-entry patch applies; native layout preserved. Changed-entry destinations verified.
</pre>

```diff
--- a/README.md
+++ b/README.md
@@ -329,7 +329,7 @@
 - [lavish](https://github.com/mquan/lavish) - A color scheme generator (using Rails 4.2).
 - [lifeToRemind](https://github.com/eduqg/LifeToRemind) - A career planning app (using Rails 5.2).
 - [Listopia](https://github.com/spaquet/listopia) - A modern list / task management app (using Rails 8). - [:earth_africa:](https://listopia-dhv.pages.dev)
-- [lobsters](https://github.com/lobsters/lobsters) - A link aggregation app (using Rails 7.0). - [:earth_africa:](https://lobste.rs)
+- [lobsters](https://github.com/lobsters/lobsters) - A link aggregation app (using Rails 8.1). - [:earth_africa:](https://lobste.rs)
 - [loomio](https://github.com/loomio/loomio) - A collaborative decision-making app (using Rails 6.1). - [:earth_africa:](https://www.loomio.com/)
 - [mastodon](https://github.com/mastodon/mastodon) - A microblogging app (using Rails 6.1). - [:earth_africa:](https://mastodon.social/about)
 - [maybe](https://github.com/maybe-finance/maybe) - The personal finance app for everyone (using Rails 7.2.2). - [:earth_africa:](https://maybefinance.com/)
```
