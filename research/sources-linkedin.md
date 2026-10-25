# Sources: LinkedIn deep dive (researched 2026-10-25)

This research feeds `marketing-engine/references/linkedin-playbook.md`, `styles/linkedin.json` and the `linkedin-founder-video` preset.

**Labels**
- **[O]**: official LinkedIn or regulator.
- **[R]**: research. This covers van der Blom's Algorithm InSights (secondary research) and LinkedIn papers.
- **[R-v]**: vendor dataset.
- **[P]**: practitioner.

## Official LinkedIn sources [O]

**Feed and algorithm**
- **Feed rebuild** (Engineering blog, 2026-03-12, H. Danchev): a single LLM dual-encoder handles retrieval and a Generative Recommender handles ranking. https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed
  - Summary: https://ppc.land/linkedin-rebuilds-its-feed-from-scratch-with-llms-and-gpu-powered-ranking/
- **"Updates to the LinkedIn Feed"** (Tim Jurka, 2026-03-12). This update demotes four things: engagement bait, poll-baiting, recycled thought leadership, and video that doesn't match its text. LinkedIn also says pods and automation are being made ineffective. https://www.linkedin.com/pulse/updates-linkedin-feed-focusing-authentic-relevant-tim-jurka-umwnc/
- **AI-slop report button** and rollback of the "enhance post" feature (2026-07-30, CPO Hari Srinivasan, as reported by Bloomberg Gov). https://news.bgov.com/artificial-intelligence/linkedin-is-cracking-down-on-ai-slop-with-new-reporting-tool
- **Creator Mode removed** (2024). https://www.socialmediatoday.com/news/linkedins-removing-creator-mode-option/706585/
- **Top Voice badge** for collaborative articles retired (2024-10-08). https://www.socialmediatoday.com/news/linkedins-removing-top-voice-badges-collaborative-articles/728247/
- **Commenting can triple profile views** (LinkedIn creator account, as reported). https://www.lindseygamble.com/blog/linkedin-shares-commenting-can-triple-profile-views

**Analytics**
- Saves and sends metrics added (2025-09). https://www.socialmediatoday.com/news/linkedin-adds-save-and-send-data-to-content-insights/759828/
- Profile viewers and followers gained per post. https://lindseygamble.com/blog/linkedin-expands-analytics-with-saves-sends-metrics

**Formats and specs**
- **Newsletters**: subscribers are notified, and followers are auto-invited. https://www.linkedin.com/help/linkedin/answer/111414
- **Video specs**:
  - Organic: https://www.linkedin.com/help/linkedin/answer/a7486279
  - Ads: https://www.linkedin.com/help/linkedin/answer/85306
- **LinkedIn Live access**: https://www.linkedin.com/help/billing/answer/a568503
- **Vertical video feed**: uploads up 36% (TechCrunch, 2025-02-04). https://techcrunch.com/2025/02/04/linkedin-amps-up-vertical-video-tools-as-uploads-jump-36
- **BrandLink**: https://news.linkedin.com/2025/helping-brands-expand-their-reach-in-new-ways-with-video-from-to
- **Company Page best practices**: posting weekly gives 2x engagement, and complete pages get 30% more views. https://business.linkedin.com/marketing-solutions/company-pages/best-practices

**Ads**
- **Thought Leader Ads**: https://business.linkedin.com/advertise/ads/sponsored-content/thought-leader-ads
- **Document Ads** (lead gating via the API): https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/advertising-targeting/version/document-ads
- **Matched audiences**: minimum 300 members. https://www.linkedin.com/help/lms/answer/a423690
- **Message ads**: opt-in required in the EEA and Switzerland. https://www.linkedin.com/help/lms/answer/a427509
- **Budgets**: https://business.linkedin.com/marketing-solutions/success/best-practices/maximize-your-budget

## Research [R]

**Van der Blom, Algorithm InSights 2025** (about 1.8M posts)
- Report figures as given in interviews:
  - https://www.youtube.com/watch?v=nmPGcQvDnEg
  - https://www.youtube.com/watch?v=mymPtjd48KQ
- Secondary write-ups:
  - https://www.socialpilot.co/blog/linkedin-algorithm
  - https://www.leptidigital.fr/reseaux-sociaux/reach-organique-linkedin-effondrement-85145/
- **Caveat:** the headline figures conflict across write-ups (47/39/42 vs 50/25/59).

**Other research**
- **LinkedIn 360Brew paper** (2025-01). It is unconfirmed whether this is the production model.
- **B2B Institute / Ehrenberg-Bass 95:5 rule** (2021). This is a heuristic.

## Vendor and practitioner sources [R-v] / [P]

**Vendor datasets [R-v]**
- **Ordinal link-penalty study**: 900k posts, 26.5% penalty. https://www.tryordinal.com/blog/linkedin-link-penalty-study
- **ConnectSafely edit test** (2026): 340 posts. https://connectsafely.ai/articles/does-editing-linkedin-post-affect-reach-2026
- **Hootsuite long vs short comments** test (small n). https://blog.hootsuite.com/long-vs-short-linkedin-comments/
- **Ad benchmarks**:
  - ZenABM 2026: https://zenabm.com/blog/linkedin-ads-benchmarks-2026
  - Dreamdata: https://dreamdata.io/blog/linkedin-ads-benchmarks
  - Huble: https://www.huble.com/blog/linkedin-ads-benchmarks
- **Character limit / fold**: https://contentin.io/glossary/character-limit/

**Practitioners [P]**
- **SLAY framework** (Lara Acosta): https://cool-story.beehiiv.com/p/lara-acosta-slay-framework
- **Content OS** (Justin Welsh): https://learn.justinwelsh.me/the-content-os

## Singapore health advertising (clinic directors)

- **HCS (Advertisement) Regulations 2021 and MOH FAQ**: the full text could not be fetched (404/403). Our rules rest on MOH excerpts and secondary summaries.
- **SMC Ethical Code and Ethical Guidelines (2016)**: the testimonial ban was checked via the SMA reproduction.
- **MOH review of allied-health advertising** (2025-03-07). https://www.marketing-interactive.com/moh-to-review-advertising-restrictions-for-healthcare-professionals

## Gaps (verify before hard-coding numbers)

- Exact van der Blom 2025 and 2026 figures.
- Link and edit penalty sizes, and the golden-hour window.
- AHPC physio advertising clauses.
- Implementation status of the MOH review.
- Thought Leader Ad eligibility for articles and newsletters.
- Status of Conversation Ads in SG and the UK.
- The "13% Lead Gen Form conversion" figure.
