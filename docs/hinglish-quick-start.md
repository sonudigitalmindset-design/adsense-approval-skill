# Hinglish Quick Start

Ye skill Google AdSense approval ke liye hai. Ye AI
assistant aur insaan dono ke liye bani hai. Isme official
rules, audit scripts, rejection fix plans, aur approved
account ko safe rakhne ke tareeke hain.

[Back to the main page](../README.md)

## Skill kya hai

AdSense approval ek poori site ki review hoti hai. Google
sirf homepage nahi dekhta. Har page, har menu, har policy
page, aur site ka behaviour dekha jata hai. Ye skill wahi
check karna sikhati hai jo check ho sakta hai, aur saaf
saaf batati hai jo koi script check nahi kar sakti.

Ek baat shuru me hi saaf hai. Koi bhi skill approval ki
guarantee nahi de sakti. Google decide karta hai. Jo ye
daava kare ki approval pakka milega, woh jhooth bol raha
hai. Ye skill imaandaar taiyaari karwati hai, guarantee
nahi deti.

## Shuru kaise karein

Sabse pehle ye padhein:

1. [Understanding AdSense approval](understanding.md):
   review kaise kaam karta hai, aasan bhaasha me.
2. [How to use this skill](usage.md): pehli site,
   rejection, aur approved account ke workflows.
3. `references/02-eligibility-and-application.md`:
   official eligibility aur application steps.
4. `references/08-pre-apply-checklist.md`: apply karne
   se pehle ki checklist.

Phir audit scripts chalaiye.

## Audit kaise chalaye

Do scripts hain. Dono read-only hain. Dono sirf Python
standard library use karte hain. Dono site me koi badlaav
nahi karte.

Pehla, chhota checker:

```bash
python3 scripts/site_audit.py https://example.com
```

Ye homepage, robots.txt, ads.txt, trust pages, aur
buniyaadi cheezein check karta hai. Shuruaat yahin se
karein.

Dusra, deep audit:

```bash
python3 scripts/deep_audit.py https://example.com --output report.md --json report.json
```

Ye sitemap ke har page ko crawl karta hai. Titles,
descriptions, headings, images, links, canonicals,
noindex flags, aur bahut kuch check karta hai. Badi site
par isme ek ya do minute lag sakte hain. `--workers 2`
se dheeme hosting par load kam hota hai.

## Score ka matlab

Deep audit ek readiness score deta hai, jaise 90/100. Ye
score samajhna bahut zaroori hai.

- Ye Google ka score NAHI hai. Google aisa koi score
  publish nahi karta.
- Ye sirf ye batata hai ki machine se check hone wali
  cheezon me kitna kaam baaki hai.
- 100/100 ka matlab approval pakka NAHI hai. Content ki
  quality, originality, traffic quality, aur account
  history koi script nahi dekh sakti.
- Score ko ranking ki tarah use karein, faisle ki tarah
  nahi. Pehle failures fix karein, phir warnings ko page
  kholkar khud padhkar decide karein.

## Apply karne se pehle

1. Audit ke saare failures fix karein aur live verify
   karein.
2. Har warning ko khud padhein. Kuch warnings asli
   problem nahi hoti.
3. Trust pages publish karein: About, Contact, Privacy
   Policy, aur zaroorat ho to Terms aur Disclaimer.
   Apne shabdon me likhein, template copy paste na
   karein.
4. Site ko phone par khud kholkar dekhein. Menu, layout,
   aur consent banner check karein.
5. Sitemap aur Search Console me indexing check karein.
6. Phir apply karein, aur review ke dauraan verification
   code ko hataayein nahi.

Poori checklist yahan hai:
`references/08-pre-apply-checklist.md`.

## Rejection aaye to kya karein

1. Sites page par exact reason aur date note karein.
2. `references/07-rejection-reasons-and-fixes.md` me
   us reason ka fix plan padhein.
3. Poori site audit karein. Har kamzor page fix karein,
   sirf do chaar nahi.
4. Fix live verify karein, phir review request karein.
5. Bina badlaav ke dobara apply na karein. Approval
   services ko paise na dein. Koi dusra account na
   banayein.

## Official, reported, aur andaza: farq samjhein

Skill me har daave par label hota hai.

- OFFICIAL: Google ke Help page par live padhkar likha
  gaya hai, link aur date ke saath.
- REPORTED: kisi doosre source se aaya hai, source ka
  naam likha hota hai. Ye Google ka rule nahi hai.
- INFERRED: rejection patterns se nikala gaya andaza
  hai. Ye kabhi Google ka rule batakar nahi sikhaya
  jata.

Agar live official page aur skill me farq dikhe, to
official page sahi mana jata hai. Skill update karne ke
liye [Contributing](contributing.md) padhein.

## Aur kahan padhein

- [Contents](contents.md): skill ki har file ka link.
- [FAQ](faq.md): chhote, imaandaar jawaab.
- [Staying updated](staying-updated.md): official
  badlaav par nazar kaise rakhein.
- `references/37-india-publishers-guide.md`: India ke
  publishers ke liye payments, tax, aur consent law.
- `references/38-wordpress-and-site-kit-setup.md`:
  WordPress par code lagane ke practical steps.
