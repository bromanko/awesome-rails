# Freshness research

Advisory only; every suggested change requires maintainer review.
No list edits, PRs, comments, or reviews were submitted.

Catalog revision: `2e1263442ed11b98dff1f2aacff2039571315f53`
Slice: 0 of 139 (zero-based)
Catalog recheck: unchanged

Sources below are agent-reported observations, not independent verification.

## Entry 32

<pre>Rails Official Guide

The canonical URL resolves directly (HTTP 200, no redirect) to the official Ruby on Rails Guides, titled &quot;Ruby on Rails Guides&quot;, currently for v8.1.x. The name matches. The entry has no description to correct.

https://guides.rubyonrails.org
Returns HTTP 200 with no redirect. The page title is &quot;Ruby on Rails Guides&quot;, and the version selector lists v8.1.4.1, v8.0, v7.2, v7.1, which shows these are the official guides for current Rails.

Blocking uncertainties:
None reported.

Informational caveats:
Checked only that the page responds, plus its title and version list. Did not review the guide content.

Recommendation: keep
Proposed name: None
Proposed URL: None
Proposed description: None</pre>

## Entry 242

<pre>FAE

The label &quot;(using Rails 5.2)&quot; is out of date. The repo&#x27;s Gemfile pins the dummy app to rails ~&gt; 7.0.2, Gemfile.lock resolves rails 7.0.2.3, and the README says &quot;Fae 3.x supports Rails 7. For legacy Rails support you can use Fae 2.x on Rails 5.0 to 5.2.&quot; The gemspec (version 3.1.0) declares rails &gt;= 5.0. Rails 5.2 comes only from a legacy Appraisals file and the 2.x line. The name, URL and CMS-by-FINE description all still hold: the repo is not archived and its description is &quot;CMS for Rails. For Reals.&quot;. The trailing period that the first entry lacks is left as is to keep the change minimal.

https://github.com/wearefine/fae/blob/master/Gemfile
Contains `gem &#x27;rails&#x27;, &#x27;~&gt; 7.0.2&#x27;` with the comment &quot;Set the version of Rails for the dummy app&quot;.
https://github.com/wearefine/fae/blob/master/Gemfile.lock
Resolves `rails (7.0.2.3)` and `railties (7.0.2.3)`.
https://github.com/wearefine/fae/blob/master/README.md
Says &quot;CMS for Rails. For Reals.&quot; and &quot;Fae 3.x supports Rails 7. For legacy Rails support you can use Fae 2.x on Rails 5.0 to 5.2.&quot;
https://github.com/wearefine/fae/blob/master/fae.gemspec
Gem fae-rails, version 3.1.0, author FINE. Declares `s.add_dependency &#x27;rails&#x27;, &#x27;&gt;= 5.0&#x27;`.
https://github.com/wearefine/fae/blob/master/Appraisals
Lists only legacy appraisals for rails_5_0, rails_5_1 and rails_5_2. This is older test-matrix configuration, not the current main dependency.
https://api.github.com/repos/wearefine/fae
Repo wearefine/fae is not archived, the default branch is master, the description is &quot;CMS for Rails. For Reals.&quot;, and the homepage is https://www.faecms.com.

Blocking uncertainties:
None reported.

Informational caveats:
Fae is a Rails engine (gem) rather than a standalone app, but this section already lists it. Section placement was not re-evaluated.
The version label is based on declared dependencies only. Runtime compatibility was not tested.
The canonical URL in the entry has a trailing slash. It resolves to the same repo and was left unchanged.

Recommendation: update
Proposed name: None
Proposed URL: None
Proposed description: A modern CMS developed by FINE (using Rails 7.0)</pre>

## Entry 259

<pre>canvas-lms

instructure/canvas-lms is Instructure&#x27;s active, unarchived, open-source LMS. &quot;A learning management app.&quot; is accurate. The entry has no version label to go stale; the declared dependency is currently rails ~&gt; 8.0.0 (locked at 8.0.5). Adding a label would be optional, not a correction.

https://github.com/instructure/canvas-lms/blob/master/README.md
Says &quot;Canvas is a modern, open-source LMS developed and maintained by Instructure Inc.&quot;
https://api.github.com/repos/instructure/canvas-lms
Repo is not archived, the default branch is master, the description is &quot;The open LMS by Instructure, Inc.&quot;, and the last push was 2026-04-30.
https://github.com/instructure/canvas-lms/blob/master/Gemfile.d/app.rb
Declares `gem &quot;rails&quot;, &quot;~&gt; 8.0.0&quot;`. Gemfile.lock resolves rails (8.0.5).

Blocking uncertainties:
None reported.

Informational caveats:
Did not run or install the app.
The current entry has no version label. Adding &quot;(using Rails 8.0)&quot; would be optional and is not proposed here.

Recommendation: keep
Proposed name: None
Proposed URL: None
Proposed description: None</pre>


# Proposed pull requests

1 proposed change(s); 0 held for unresolved questions.

### Ready for maintainer review
<pre>related: Both queries found FAE records, but neither proposes or objects to changing the Rails version label. PR #83 (merged 2021-10-12) first added the entry as &#x27;A modern CMS deveveloped by FINE (using Rails 5.2)&#x27;. That explains where the 5.2 label came from: it was accurate when the entry was added. Issue #106 asked for the typo &#x27;deveveloped&#x27; to be fixed. It was closed as completed, and a collaborator thanked the reporter. The current entry text already says &#x27;developed&#x27;, so that fix is in. Neither record discusses Rails 7, Fae 3.x or updating &#x27;(using Rails 5.2)&#x27;. There is no open PR with the same correction and no maintainer rejection, so this is related context rather than a duplicate, rejection or obsolete result. The search covered only the two listed queries in gramantin/awesome-rails.
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
repo:gramantin/awesome-rails &quot;FAE&quot; in:title,body,comments
repo:gramantin/awesome-rails &quot;https://github.com/wearefine/fae/&quot; in:title,body,comments
References:
https://github.com/gramantin/awesome-rails/pull/83
https://github.com/gramantin/awesome-rails/issues/106
https://github.com/gramantin/awesome-rails/issues/106#issuecomment-1612714195</pre>

## entry-242

<pre>Update FAE entry

The label &quot;(using Rails 5.2)&quot; is out of date. The repo&#x27;s Gemfile pins the dummy app to rails ~&gt; 7.0.2, Gemfile.lock resolves rails 7.0.2.3, and the README says &quot;Fae 3.x supports Rails 7. For legacy Rails support you can use Fae 2.x on Rails 5.0 to 5.2.&quot; The gemspec (version 3.1.0) declares rails &gt;= 5.0. Rails 5.2 comes only from a legacy Appraisals file and the 2.x line. The name, URL and CMS-by-FINE description all still hold: the repo is not archived and its description is &quot;CMS for Rails. For Reals.&quot;. The trailing period that the first entry lacks is left as is to keep the change minimal.

Evidence:
https://github.com/wearefine/fae/blob/master/Gemfile — Contains `gem &#x27;rails&#x27;, &#x27;~&gt; 7.0.2&#x27;` with the comment &quot;Set the version of Rails for the dummy app&quot;.
https://github.com/wearefine/fae/blob/master/Gemfile.lock — Resolves `rails (7.0.2.3)` and `railties (7.0.2.3)`.
https://github.com/wearefine/fae/blob/master/README.md — Says &quot;CMS for Rails. For Reals.&quot; and &quot;Fae 3.x supports Rails 7. For legacy Rails support you can use Fae 2.x on Rails 5.0 to 5.2.&quot;
https://github.com/wearefine/fae/blob/master/fae.gemspec — Gem fae-rails, version 3.1.0, author FINE. Declares `s.add_dependency &#x27;rails&#x27;, &#x27;&gt;= 5.0&#x27;`.
https://github.com/wearefine/fae/blob/master/Appraisals — Lists only legacy appraisals for rails_5_0, rails_5_1 and rails_5_2. This is older test-matrix configuration, not the current main dependency.
https://api.github.com/repos/wearefine/fae — Repo wearefine/fae is not archived, the default branch is master, the description is &quot;CMS for Rails. For Reals.&quot;, and the homepage is https://www.faecms.com.

Informational caveats:
Fae is a Rails engine (gem) rather than a standalone app, but this section already lists it. Section placement was not re-evaluated.
The version label is based on declared dependencies only. Runtime compatibility was not tested.
The canonical URL in the entry has a trailing slash. It resolves to the same repo and was left unchanged.

Based on catalog revision 2e1263442ed11b98dff1f2aacff2039571315f53.
Proposed by an automated freshness review. A maintainer must verify the evidence and edit.
Validation and discussion checks are recorded below.

Review status: Ready for maintainer review
Prior discussion: related: Both queries found FAE records, but neither proposes or objects to changing the Rails version label. PR #83 (merged 2021-10-12) first added the entry as &#x27;A modern CMS deveveloped by FINE (using Rails 5.2)&#x27;. That explains where the 5.2 label came from: it was accurate when the entry was added. Issue #106 asked for the typo &#x27;deveveloped&#x27; to be fixed. It was closed as completed, and a collaborator thanked the reporter. The current entry text already says &#x27;developed&#x27;, so that fix is in. Neither record discusses Rails 7, Fae 3.x or updating &#x27;(using Rails 5.2)&#x27;. There is no open PR with the same correction and no maintainer rejection, so this is related context rather than a duplicate, rejection or obsolete result. The search covered only the two listed queries in gramantin/awesome-rails.
Validation: One-entry patch applies; native layout preserved. Changed-entry destinations verified.
</pre>

```diff
--- a/README.md
+++ b/README.md
@@ -239,7 +239,7 @@
 
 > Note: Rails versions of these apps are valid as the date of latest commit. They are defined in their Gemfile and/or Gemfile.lock and they might be outdated. If you find it outdated, don't forget to notfiy us by opening a pull request.
 
-- [FAE](https://github.com/wearefine/fae/) - A modern CMS developed by FINE (using Rails 5.2)
+- [FAE](https://github.com/wearefine/fae/) - A modern CMS developed by FINE (using Rails 7.0)
 - [activeWorkflow](https://github.com/automaticmode/active_workflow) - An intelligent process and workflow automation platform based on software agents (using Rails 6.0).
 - [adopt-a-hydrant](https://github.com/codeforamerica/adopt-a-hydrant) - A civic infrastructure detection app (using Rails 4.2).
 - [airCasting](https://github.com/HabitatMap/AirCasting) - A platform for recording, mapping, and sharing health and environmental data using your smartphone (using Rails 6.1). - [:earth_africa:](https://www.habitatmap.org/aircasting)
```
