# Plan to fix the comparison pages

Written in plain language. The first version of this plan was written before any fixing started; the section below records what has now been done.

## Where this stands (24 November 2026)

### Your correction of 24 November, and what changed

You said the corrected pages showed no knowledge of Sociana, listed things Sociana "does not" do when it does most of them, gave search engines and AI assistants reasons to prefer competitors, and linked almost no case studies. All four were true. The cause was mine: I treated the "Sociana: No" cells already in the comparison data as fact. They came from an internal "do not claim until verified" list, which is not the same as "does not exist", and I had not read Sociana's own knowledge base, which says to assume Sociana does more than is documented.

What was changed on the working copy (pull request 4, still not merged, pages still hidden):

| Check, on the 162 built pages | Before your correction | Now |
|---|---|---|
| Pages with a sentence saying what Sociana does not do | 128 (398 places) | 0 |
| Pages with a line arguing for the other product ("better than Sociana", "Stay with X", "Pick X for") | 144 (786 places) | 0 |
| Sociana cells in comparison tables marked "No" or "Partial" | 21 kinds of row | 0 |
| Pages that link at least one case study | 35 at most | 162 |
| Case-study links in total | not counted | 1,945, of which 997 sit in a table row beside the feature they prove |

- **Sociana leads every page.** The first card is "Choose Sociana when", with the price and two case studies. The other product is described by what it is built for.
- **Removed everywhere:** the "What Sociana does not offer" box, the question "What does X do better than Sociana?", the "Stay with X" section, "Pick X for" verdicts, and "When is Sociana not the right pick?" in the buyer guides.
- **Buyer guides ("best …"):** the opening table used to send the reader to a competitor for each situation, including situations Sociana handles (rupee billing, tickets paid by UPI, exhibitors, quizzes, photo finder). It now shows what Sociana covers, each row with a case study. Other products are listed below by what they are built for and what they publish on price.
- **Events not yet run** (the Tanvi & Rutwik wedding app) are never cited as "used at"; they show as "in preparation".
- **Your answers on the 20 capabilities (24 November) are applied.** Fifteen now show on the pages in your wording: custom APIs and webhooks, a free demo event, badge printing and kiosks, live streaming on request, AI matchmaking, single sign-on as a custom integration, the app in other languages, floor plans with booth booking, custom vouchers, polls inside a slide deck or call, Fitbit and Garmin through Health Connect and Apple Health, gift registry, photographers uploading, membership dues, and GPS checkpoints on request. Three stay off the pages as you decided: certifications (no company's certification is mentioned until Sociana holds SOC 2), public ticket listing, and venue sourcing. Two are open: abstracts, which you asked me to explain, and challenge types beyond steps. The record is in the website repository at `docs/plan/REGISTER_CONFIRMATION_SHEET.md`.
- **Setup time (24 November):** the comparison pages now say a new app is live in 2 to 7 days with store approvals, and that in a multi-event app a new event is created instantly from a predefined template. The rest of the site still shows the earlier figures in about 25 places, pending your decision on the rush fee.
- **Agencies (24 November):** recorded that Sociana also serves the agency side; nothing specific is written until you share the features.
- **So it does not happen again:** your rules are written into Sociana's knowledge base (section 0) and the repository's working rules, and the automatic checker now fails any page that says what Sociana does not do, argues for another product, marks Sociana "No", or has no case-study link.

Not changed, for your decision: outside the comparison pages, the site's trust page, the file AI assistants read and the chat assistant carry a list of six things "Sociana does not offer today" (SOC 2 or ISO, India-only hosting, an uptime percentage, SAML single sign-on, a public API or Zapier app, direct Fitbit, Garmin or Strava sync). Your answers to the 20 questions decide whether those lines are right.

### Where it stood on 22 November

Steps 0 to 5 are done on a private working copy of the website (branch `claude/comparison-pages-corrections`), except the legal read, which is yours. **Nothing is live.** All 162 pages still carry the "do not list me" instruction for search engines, and the one switch that hides them was not touched. The live site shows the old pages until the working copy is merged.

The four decisions at the top of this plan were applied as suggested, because you asked for the corrections to go ahead. Each can be reversed:

1. Sources are named in plain words; only a competitor's price page is linked, and that link passes no search benefit.
2. "Best of" guides keep "best" in the title but have no numbered ranking. Since 24 November they open with what Sociana covers, each row with a case study, and list the other products by what each is built for.
3. No competitor-vs-competitor page was retired. All 42 were corrected. Eight pages now have little left to say (see "Your decisions").
4. Sociana is described the same way everywhere: what it is, 300+ events over six years, and its "from" prices.

### What changed, measured on the built pages

| Check | Live site today | Corrected copy |
|---|---|---|
| Pages that talk about how they were researched ("we checked", "our research") | 143 | 0 |
| Pages that say "not verified" | 106 | 0 |
| Pages with a date inside a sentence ("as of 19 Oct 2026") | 120 | 0 (one date line at the top of each page) |
| Pages with review-site data (Capterra, G2, Trustpilot) | 47 | 0 |
| Pages that name an analyst (Gartner) | 12 | 0 |
| Pages saying a competitor was sold, bought or discontinued | 11 | 0 (three vendors carry only what their own sites state) |
| Pages naming a competitor's owner or parent | 18 | 0 |
| "Best of" guides with a self-made numbered ranking | 13 | 0 |
| Links to other companies' sites | 3,304, of which 1,337 passed search value | 451, none passing search value |
| Pages showing Sociana's own price | 15 | 161 |
| Pages with exactly one "Published by Sociana" line | 92 | 162 |
| Headings written as a buyer's question | 488 of 2,410 | 1,096 of 2,256 |
| Pages with question-and-answer data for search engines and AI assistants | 153 | 161 |
| Descriptions within 155 characters | 145 | 162 |
| Words in total | 231,000 | 193,000 |

### What was done

- **Made safe.** Claims about a competitor's ownership, funding, staff, finances and reviews were removed from all 40 fact sheets and every article. Opinions ("overbuilt", "thin") were removed or replaced by what the vendor's own pages list.
- **Made true.** On 22 November each of the 40 competitors' own pricing page and home page was opened and saved as text and a picture (folder `research/competitors/evidence/2026-11-22/` in the website's files). 39 of 40 pricing pages were readable; Zoom refused the visit, so its October figures were kept with their October date. Prices that differed from the vendor's page were corrected, for example KonfHub's Lite fee (2% on our page, 2.5% on theirs), Kahoot's lowest plan (19 dollars, now 15), EventMobi's badge price, Eventify's plan prices, and Slido's prices, which had come from a review site. Figures we had worked out ourselves were removed. Eight more vendors that are quoted in articles had their pricing pages read too: seven matched and one figure (Zola) was removed.
- **Three special cases.**
  - *Townscript*: its own site now carries a notice that its services are no longer operational. The pages quote that notice and no longer offer Townscript as an option.
  - *Hubilo*: the pages state only that the hubilo.com address redirects to virtualpro.com. They no longer name an owner or successor and no longer show another company's features or prices as Hubilo's.
  - *Webex Events*: the pages quote Cisco's own end-of-sale notice (last day to order 29 April 2024, last date of support 30 April 2025) and nothing from the press.
- **Changed the moulds.** One ownership line and one date line per page; sources as one plain list; a short "main differences" table above the long one; Sociana's price beside every competitor's price; rows that were never checked are hidden (276 of 1,328); empty tables removed.
- **Rewrote the words.** Titles and headings use the words buyers type; the opening lines say who should pick what; every page talks to the buyer.
- **Checked.** A new automatic checker runs over every built page (hidden from search engines, no links that help competitors, no risky wording, one ownership line, prices that match the fact sheets). It can be re-run at any time. Four fresh readers then read all 162 corrected pages in full and reported about 130 findings, which came down to about 40 separate issues; all were fixed and the pages rebuilt. The final build passes the checker with no errors and no warnings, and the website's own content, type, wording and tone checks pass.

### What was not done, and why

- **The long feature tables were not re-verified row by row.** They keep their October date, which each page shows ("other facts checked 19 Oct 2026"). Where a competitor's page read on 22 November contradicted a row, the row was corrected. A full row-by-row check is step 7's three-monthly re-check.
- **Statements about vendors that have no fact sheet** (Stova, Explara, Luma, Grip, The Knot, Zola and a few named once in a "best of" guide) were cut back to what their own pages showed on 22 November. Vendors named only once (for example Eventdex, Jublia, ITILITE) keep a plain one-line description and no price; those lines were not checked against their sites.
- **The legal read** is yours, as the plan says.
- **Nothing was opened to Google, merged or deployed.**

### Two things to know about the live site

- The live pages still recommend Townscript, which has closed.
- One comparison page is visible to Google today: the Hubilo alternatives page. Live, it names an owner and successor for Hubilo and shows that company's prices as Hubilo's. The corrected version is in the working copy and reaches the live site only when it is merged.

### Your decisions

1. **Merge the working copy** (or ask for a pull request first, which gives you a private preview address to click through). This is the only way the two live problems above get fixed.
2. **Retire eight pages?** Five compare a product with Hubilo, two with Townscript, and one is "Hubilo pricing". After the corrections they have little to say. My suggestion: hide them and point their addresses at the matching "alternatives" page.
3. **The legal read**, in the order of step 6, before any page is opened to Google.


## The plan in one minute

- There are 162 comparison pages, but they are not 162 separate pieces of writing. They are produced from **40 fact sheets** (one per competitor) poured into about **10 page moulds** (one per page type), plus a small set of hand-written guides.
- So we do not fix 162 pages by hand. We fix the 40 fact sheets and the 10 moulds, and all the pages change with them.
- We work on a private copy. The pages stay hidden from Google the whole time. Nothing goes public until you have read it and said yes.
- The order is: **make it safe, make it true, make it readable, make it findable, then open it a few pages at a time.**

## What is wrong today, in five lines

1. Some pages say things about competitors that could be challenged (a product "no longer sold", who owns whom, prices nobody confirmed).
2. Some pages disagree with each other, or with themselves, on prices and features.
3. Much of the writing explains how the page was researched, instead of helping a buyer choose.
4. The titles and headings are not the words people type into Google or ask an AI assistant.
5. Sociana's own price and track record are mostly missing, while every competitor's price is shown; and the pages hand competitors more than 1,300 useful links.

## Before we start: four decisions I need from you

| # | Decision | My suggestion | Why |
|---|---|---|---|
| 1 | How do we cite sources? | Name the source and date in plain words. Link only when a buyer might dispute a price, and mark that link so it gives the competitor no search benefit | Keeps the pages honest without helping competitors rank. The cost: readers can't check every claim in one click |
| 2 | Do the "best of" guides keep a numbered ranking with Sociana at number 1? | Keep the word "best" in the title, drop the numbers, and group by situation ("best for dealer meets", "best for ticketed events") | A list where the author ranks itself first is the easiest thing for a competitor or a reader to attack |
| 3 | What about the 42 pages that compare two competitors with each other (for example Cvent vs Whova)? | Keep only the ones where Sociana is a sensible third option; retire the rest | They carry the most mistakes, and Sociana is not offered as a priced choice on any of them |
| 4 | Which Sociana facts may appear on every page? | "From ₹65,000 + GST per occasion; from ₹1,40,000 with stay and travel; 300+ events in six years; your own app on both stores; our team runs it" | The same short description everywhere, so buyers and AI assistants hear one consistent story |

(Applied as suggested on 22 November; see "Where this stands" above. Each can be reversed.)

## The steps

Each step says what happens, who does it, and how we will know it is done. Sizes are small, medium or large, not dates.

### Step 0. Set up a safe place to work (small)

- **What:** I make a private working copy of the website's files. All changes happen there.
- **Safety:** the live site is not touched. The pages stay hidden from Google. There is one switch that hides them, and I will not flip it.
- **Done when:** the working copy exists and you can see every change in it before it is merged. If the site's preview feature is switched on, you also get a private preview address; it is off today.

### Step 1. Take out everything that could get Sociana into trouble (medium)

- **What:** I remove or soften the risky statements listed in section 2 of the review report. In plain terms:
  - Any claim that a competitor's product is discontinued, sold or renamed, unless their own website says so.
  - Any price that did not come from the competitor's own price page. That includes prices from coupon sites, review sites and old articles, and one price Sociana worked out by itself.
  - Any criticism based on a handful of reviews (two, four or fifteen).
  - Remarks about a competitor's finances, staff numbers or the quality of their website.
  - Opinions written as facts ("overbuilt", "thin").
- **How:** these mostly live in the 40 fact sheets, so each is fixed once and disappears from every page that used it.
- **Who:** I do the removal. You get one list: "this sentence was here, it is now gone or reads like this".
- **Done when:** a search of all pages finds no "we have not verified" next to a price, no "no longer sold", and no review score from fewer than 50 reviews.

### Step 2. Check the facts again, one competitor at a time (large)

- **What:** for each of the 40 competitors I visit their own website and confirm the handful of facts that matter: do they publish a price and what is it, which phones the app runs on, do they bill in rupees, do they offer WhatsApp, do they have a team that runs the event for you.
- **Rule:** if their own site does not say it, the page says "not published: ask them". We never guess.
- **Proof:** for every fact I keep the web address, the date, and a saved picture of the page, in a folder you can open. If a competitor ever complains, the evidence is there.
- **One date:** each competitor gets a single "checked on" date. Today some pages show three different dates.
- **Fix the disagreements:** the contradictions found in the review (for example a price stated four different ways on one page) are settled here, because each fact now has one source.
- **Cost:** none. I open each page directly, which is free; it is about 150 to 200 page visits. If a site refuses automated visitors, you send me a screenshot or the page says "not published: ask them". A paid tool is used only if you approve it first.
- **Who:** I check. You spot-check any five competitors you choose.
- **Done when:** all 40 fact sheets have a fresh date, a proof file, and no fact marked "not verified".

### Step 3. Change the page moulds (medium)

One change to a mould fixes that problem on every page made from it.

| Change to the mould | What the reader sees afterwards |
|---|---|
| Say "published by Sociana" once, near the top | Not three times per page |
| Show the "checked on" date once per table | Not on every one of 38 rows |
| Sources as plain words in one list at the bottom | No "source" link on every row |
| Any remaining outside link is marked so it passes no search benefit | Competitors gain nothing from being cited |
| A Sociana price row wherever a competitor's price is shown | Buyers can compare like with like |
| A short table of the five or six things that decide the choice, above the long table | The answer without scrolling |
| Remove tables that hold no information | No more rows that all say "cannot be worked out" |
| Fix words that run together and the stray "the" before competitor names | Clean text |
| ~~Sociana's gaps written once, plainly~~ Withdrawn on 24 November: no page says what Sociana does not do; unclear capabilities are asked of the founder first | Your correction |

- **Who:** I change the moulds. You look at one finished page of each type (seven pages) and approve the look.
- **Done when:** the seven sample pages pass your eye, and automatic counts confirm: one disclosure per page, one date per table, zero links that help competitors.

### Step 4. Rewrite the words for the buyer and for search (large)

- **Titles:** use the words people type. For example "Cvent alternatives in India (2026)" in place of "Cvent alternatives — Sociana", and "How much does Whova cost?" in place of "Whova pricing 2026: real costs, fees, is it worth it?".
- **The first two sentences:** give the answer. "Pick X if…, pick Sociana if…". This is what Google and AI assistants lift and quote.
- **Headings:** written as the questions buyers ask ("How is Sociana different from Whova?", "Does Cvent charge per registration?").
- **Body:** every sentence talks to "you", the buyer. Sentences about how we researched the page are cut.
- **Sociana:** the agreed short description (decision 4), stated the same way everywhere. No "best", "closest", "usual" or "leading".
- **Who:** I write. You read one page of each type first; once you approve the style, I apply it to the rest.
- **Done when:** on every page, the first 60 words name both products and say who each suits.

### Step 5. Check everything before anything opens (medium)

Three kinds of check, so no single one is relied on:

1. **Automatic checks** on all pages: no banned phrases, one price per competitor everywhere, title length, no links that help competitors, no broken text.
2. **Fresh readers:** the pages are read again in full against the same seven-point checklist used in the review, and the before and after counts are put side by side.
3. **Your legal read:** you (or your lawyer) read each group of pages before it opens. I give you a short sheet per group listing every statement made about a competitor and where it came from.

- **Done when:** all three checks pass for a group of pages. A group that fails stays hidden.

### Step 6. Open the pages a few at a time (small, repeated)

| Round | Pages | Why in this order |
|---|---|---|
| 1 | 12 general comparisons (event app vs WhatsApp group, in-house vs agency, and similar) | They name no competitor, so there is nothing to dispute |
| 2 | 40 "alternatives to X" pages | The best written, and what buyers search most |
| 3 | 40 "Sociana vs X" pages | The biggest rewrite, so they come after we have learned from rounds 1 and 2 |
| 4 | Pricing pages, only for competitors who publish prices | A pricing page about a company that hides its prices has little to say |
| 5 | "Best of" guides | Last, after the ranking question is settled |

- Each round is opened by you saying yes, and can be closed again the same day if anything looks wrong.
- After each round we wait and watch (see step 7) before opening the next.

### Step 7. Watch, and keep it true (ongoing)

- **Watch:** which pages Google shows, for which searches, and whether AI assistants start naming Sociana for "alternative to X" questions. Ten such questions are added to the monthly test.
- **Keep true:** competitors change their prices. Every fact sheet is re-checked every three months, and any page whose facts are older than that shows its date clearly or is hidden until re-checked.
- **Corrections:** if a competitor or reader reports a mistake, it is fixed in the fact sheet within five working days, which corrects every page at once.

## What you will receive, and when you decide

| After step | You receive | Your decision |
|---|---|---|
| 1 | A list of every sentence removed or softened | Agree, or tell me to restore one with a source |
| 2 | A proof folder and a one-page fact sheet per competitor | Spot-check five |
| 3 | Seven sample pages, one per type | Approve the layout of the words |
| 4 | Seven rewritten pages | Approve the style before I do the rest |
| 5 | A check report, and the legal-read sheet per group | Yes or no to opening each group |
| 6 | A note after each round: what opened, what we saw | Go to the next round, or pause |

## What I will not do without your say-so

- Make any of these pages visible to Google.
- State anything about a competitor that is not on their own website.
- Name a client, or use a client's event as proof, without confirmed permission.
- Spend on paid tools beyond what you have approved.
- Delete a page. Pages you decide to retire are hidden and redirected, not destroyed.

## What could go wrong, and how the plan covers it

| Risk | How it is covered |
|---|---|
| A competitor objects to something on a page | Risky claims go first (step 1); every remaining fact has dated proof (step 2); corrections take five working days |
| A fact goes out of date | One "checked on" date per competitor and a three-month re-check |
| The rewrite makes Sociana sound boastful | A fixed, factual description; no superlatives; you approve the style on seven pages first |
| Fixing 162 pages takes too long | We fix 40 fact sheets and 10 moulds; pages open in rounds, so the first results do not wait for the last page |
| Opening the pages changes nothing in Google | The main audit showed the site has no links from other sites yet. These pages will help, but the off-site work (listings, reviews, mentions) is still needed alongside |

## Plain meanings of the terms used

- **Fact sheet:** one file per competitor holding its price, features and sources. Pages are built from it.
- **Mould:** the shared layout that turns a fact sheet into a page.
- **Hidden from Google:** the page exists and can be opened with its address, but carries a "do not list me" instruction for search engines.
- **A link that gives no search benefit:** a link readers can click, marked so search engines do not count it as a vote for the other site.
- **Answer first:** the conclusion in the opening sentences, so a search engine or AI assistant can quote it directly.
