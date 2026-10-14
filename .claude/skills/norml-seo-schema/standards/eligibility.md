# Schema vocabulary, requirements and search eligibility

Verified 2026-10-13. Recheck official guidance at each runtime engagement.

- Schema.org validity and Google rich-result eligibility are distinct. Do not
  promise a visual result, local-pack placement, rankings or knowledge panel.
- Google FAQ rich results stopped appearing May 7, 2026. FAQPage remains a
  Schema.org vocabulary type; there is no Google FAQ rich-result target.
  [Google documentation updates](https://developers.google.com/search/updates)
- The Sitelinks Search Box was retired in November 2024. SearchAction may describe
  a real search action but is not needed to enable that retired feature.
  [Google announcement](https://developers.google.com/search/blog/2024/10/sitelinks-search-box)
- Article properties are recommended rather than a universal required-field set.
  There is no universal 110-character headline or mandatory 1200px image rule.
  Use accurate full headings and crawlable representative high-resolution images.
  NewsArticle selection follows real news content, not registration/licensing.
  [Google Article guidance](https://developers.google.com/search/docs/appearance/structured-data/article)
- Product snippets and merchant listings have different property requirements.
  Use current docs for the chosen result; Product alone does not guarantee ratings.
  Never invent currency/availability, require fake review counts or silently default
  missing stock to InStock. Accurate zero prices must remain zero.
  [Product snippets](https://developers.google.com/search/docs/appearance/structured-data/product-snippet)
  and [merchant listings](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- ItemList alone does not make an arbitrary archive eligible for a carousel.
- Merchant-level return policies are linked under Organization; per-product policies
  use the supported Offer linkage. Check the current supported subset and real policy.
  [Google return-policy guidance](https://developers.google.com/search/docs/appearance/structured-data/return-policy)

The field tables in schemas/ are implementation planning profiles, not statements
that Schema.org or Google universally requires each suggested field. These rules
supersede older template defaults. Source templates are examples to adapt and
review; never deploy guessed values, inherited formatting mistakes or an unreviewed
field contract. ACF functions require the plugin; no code can assume it exists.
