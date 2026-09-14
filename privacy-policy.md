---
layout: default
title: "Privacy Policy"
permalink: /privacy-policy/
---

# CrazyPoly — Privacy Policy

**Effective date:** 14 September 2026
**Applies to:** CrazyPoly.

---

## 1. Who we are

CrazyPoly is made and operated by Dmytro Korchynskyi, an individual based in Ukraine, trading as **NeatHippo**. Our postal address is in §1 of the Terms and Conditions, and we will give it to you on request.

"NeatHippo" is the name the game is published under; the person responsible for it, and for your data, is the individual named above.

For everything in this policy, that individual is the **controller** of your personal data.

**Contact:** support@neathippo.com

We are a very small operation. There is no separate privacy department: the same address reaches the person who wrote the game and runs the server.

---

## 2. The short version

* **Playing the game does not require an account.** Solo games, games against robots, and games with people on the same Wi-Fi work with nothing sent to us at all.
* **There are advertisements on Android, and you can turn them off by buying "Remove Ads".** One kind you choose to watch in exchange for a coin; the other appears only when you leave a match that has finished. There are none at all on desktop or in the browser version. Ads are served by Google AdMob, and in the EEA and the UK you are asked what you allow before any personalised one is requested — see §6.9.
* **We count a few anonymous things about how the game is played, to help us improve it.** The app opening, a game starting or ending, a purchase completing, and whether finding an online match, a private room or a Wi-Fi game succeeded — tagged with a random identifier belonging to the installation and not to you or your account. See §6.10.
* **We ask for data when you want the online parts**: an account so you can play over the internet, keep your statistics across devices, hold coins, and have a friends list.
* **We do not sell personal data**, and we never have. We do not profile you: nothing we hold is used to build a picture of you as a person, and nothing about how you play is passed to anybody for their own marketing.
* **Players talk to each other with a fixed set of emoji reactions.** There is no free-text chat in CrazyPoly, which is deliberate — see §7.
* **You can delete your account from inside the game**, at any time and without asking anybody: User Account → Delete account. It takes the account and everything attached to it with it — bar one small anti-cheating marker, described in §6.8 — and it cannot be undone. If you cannot reach that button — you have lost the device, or cannot sign in — write to **support@neathippo.com** and we will do it for you.

---

## 3. What stays on your device

Whether or not you ever sign in, the game keeps its own files in its private storage on your device: your settings and preferences, your unfinished game, your statistics, your sign-in token if you are signed in, short-lived notes that let you back into a multiplayer game you were in, the random installation identifier described in §6.10, and a technical log of what the game did. We do not receive any of it, unless you deliberately send us a log yourself (see §6.7).

On the first start after updating from an earlier version of CrazyPoly, the game also reads what that version stored on your device, so that your language, player name, colour and win counters carry over. It is read only — never changed, never deleted — and nothing from it is sent anywhere.

Uninstalling the app removes all of it.

---

## 4. Accounts

An account is needed for online play, for coins, and for the friends list. Nothing else in the game requires one.

There are three ways to sign in, and they differ in what we learn about you:

**E-mail and password.** We store your e-mail address and a password that the server keeps only as a salted hash — the password itself is never stored and cannot be read back by us. Your e-mail is used to confirm the address, to reset a forgotten password, and to reach you about your account or a purchase.

**Google Sign-In.** Google returns a signed token to the game, from which the server takes a stable Google account identifier and the e-mail address on that Google account. We never see your Google password, and we do not get your contacts, your Drive, or anything else from your Google account.

**This device only.** The account is tied to a random identifier the game generates and keeps in its own private storage on the device — nothing tied to the hardware, and nothing else attached to it: no e-mail, no name from anywhere. It is the most private option and it has one important catch: because that identifier lives only in the game's own storage, **a device-only account cannot be signed back into once you sign out, uninstall the game, or lose the device.** The game warns you about this before you sign out.

Whichever route you take, the account carries a **display name** you choose. Other players see that name; pick one you are happy for strangers to see.

You can add a second sign-in method to an existing account later — for example, linking an e-mail and password to a device account so you can get back in from a new phone.

---

## 5. What the online service stores about your account

* **Account record** — account id, display name, sign-in identifiers from §4, creation and last-login times, whether the e-mail address has been confirmed.
* **E-mail confirmation and password-reset codes** — six-digit codes with a 15-minute lifetime, kept only until they are used or expire.
* **Statistics** — how many games you won, lost and abandoned, counted separately for games against people and games against robots, and per robot difficulty. These are merged with the counters on your device so that playing offline, or on a second phone, does not lose games.
* **Coins and entitlements** — your coin balance, and a record of which themes you have paid for so they survive a reinstall.
* **A starting-coins marker** — a note that the device you signed up from has already been given the free coins a new account starts with. It is kept apart from your account rather than on it, and it is the one thing that outlives the account: see §6.8 and §11.
* **Purchase records** — for each purchase through Google Play: the product id, Google's purchase token and receipt, and whether the server granted the item. We hold these so we can honour and, where needed, re-grant what you bought.
* **Friends** — the accounts you added, the requests you sent or received, and while you are signed in, a presence record saying whether you are online, roughly what you are doing, and the code of a room you are in so a friend can join you.
* **Match records** — while an online match is being played and briefly afterwards: who is at the table, the state of play, and the final result. If you drop out before a game ends, the result and final board position (about 1.5 KB) are kept on the match record so the game can tell you how it went the next time you sign in.
* **Connection data** — the server necessarily sees the IP address your device connects from, together with timestamps, in its logs.

---

## 6. What else we handle, and why

### 6.1 Playing over the internet

While you are in an online match, your display name, avatar, colour, chosen theme and every move you make are relayed through our server to the other players at the table, because that is what playing a game together means. Matches are **relayed**, not peer-to-peer: other players do not learn your IP address from the game.

### 6.2 Playing over local Wi-Fi

LAN play does not use our server at all and does not need an account. Your device announces the game on the local network and exchanges your player name, avatar and colour directly with the other devices on it. Anyone on the same network — a home router, a café hotspot — can see that announcement and the local IP address it came from. That is inherent to local play.

### 6.3 Private rooms

A private room is a six-character code. Anyone who has the code can join that room, so treat it as you would treat any invitation you read out loud.

### 6.4 Purchases

Coin packs and the Pro Pack are sold **by Google through Google Play**, not by us directly. The West theme and Remove Ads are bought with coins inside the game. Google handles the payment. We never see your card number, bank details or billing address. What we receive is the purchase token and receipt for the item, which our server checks with Google before granting anything.

"Restore Purchases" asks Google what you have bought from this app and unlocks it.

### 6.5 E-mail we send you

We send e-mail for exactly three reasons: confirming your address, resetting a password, and — rarely — telling you something important about your account or a purchase. **We do not send marketing e-mail.**

### 6.6 Server logs

The server keeps operational logs (connections, errors, request timestamps, IP addresses) so that we can keep it running and investigate abuse and faults.

### 6.7 The log you choose to send

The game can export its local log file — on Android through the share sheet, on desktop by copying it to your Downloads folder. Nothing is transmitted by that action. If you then send us that file to help with a bug report, we read it for that purpose and delete it when the matter is closed. The log contains technical events and may contain your display name; it does not contain your password.

### 6.8 Keeping the free starting coins to one per device

Every new account is given a small number of coins to start with. To stop the same person collecting them over and over by deleting an account and creating another, the game sends an identifier of the device you sign in from — on Android, the identifier Android gives our app for that device; on a computer, an identifier of the machine. Neither is an advertising identifier, and neither is the identifier used for the usage counting in §6.10 or for the ads in §6.9: this one is used for the starting coins and nothing else.

The server does one thing with it. It writes down that this device has had its starting coins, so that the next new account created on the same device does not get them again. That note holds the identifier, the date, and which account the coins went to — and nothing else: no name, no e-mail, nothing about how you play. It is not used to profile you, it is not shared with anybody, and it cannot follow you into another app.

The note is kept separately from your account, and it deliberately **survives deleting your account** (§11, §12). Delete your account and sign up again on the same device and everything else starts from nothing — but the free starting coins are not given a second time.

### 6.9 Advertising

**Ads appear on Android only.** There are none in the desktop or browser versions, and none anywhere once you have bought **Remove Ads** in the Store.

There are two kinds, and they are opposites:

* **Rewarded ads, which you ask for.** You are never shown one you did not choose. Watching one to the end credits a coin to your account. Because the coin is credited by our server rather than by the game on your device, Google is told which account is watching — your account id, and nothing else — so that it can tell our server the ad was really watched. That check is the only reason your account id reaches Google here.
* **Interstitial ads, which you do not.** One can appear when you leave a match that has already finished, and nowhere else — never during a turn, never during play — and not more often than a fixed cooldown allows. Watching one earns nothing and is not required for anything.

Ads are served by **Google AdMob**, which acts as an independent controller of the data it collects for advertising, under [Google's own privacy policy](https://policies.google.com/privacy). To choose and measure an ad, Google may use your device's advertising identifier, technical information about the device, and **your IP address** — both to work out roughly where you are and, since 3 August 2026 in the EEA, the UK and Switzerland, to recognise your device as one it has seen before.

**That last use is worth spelling out,** because an IP address does not behave like the other identifiers. An advertising identifier is stored on your device and you can reset or delete it; an IP address is stored on your device nowhere at all — it is simply part of every connection your device makes — so there is nothing there for you to clear, and neither resetting your advertising identifier nor turning off advertising cookies in your Google account settings stops Google recognising a device this way. What decides whether it may be used to *personalise* an advertisement is the consent form below: refuse personalisation and Google may not use it to build or apply a profile of you, though it will still see the address, as every server your device talks to does, and may still use it for the purposes it has a lawful basis for — measuring and securing the ads it was allowed to show. None of it is ours to switch off, because none of it is ours: it is Google's own processing as an independent controller. Buying **Remove Ads** ends the ad requests, and with them everything in this paragraph.

**We cap what an advertisement is allowed to contain.** CrazyPoly is rated 3+, and we ask Google for ads rated suitable for all audiences ("G") and nothing above it, so that an ad cannot be less suitable than the game it appears in.

**Before any of that happens in the EEA or the UK, you are asked.** The game runs Google's User Messaging Platform consent form when you first play, which is where you say what you allow and which advertising partners may take part. You can be shown that form again at any time; if you decline personalised advertising, ads still appear but are chosen without a profile of you.

Buying **Remove Ads** stops both kinds permanently on that Google account, and it is restorable on a new device through Restore Purchases.

### 6.10 Anonymous usage counting, to help us improve the game

The game counts a small number of things about how it is played, so that we can see which parts of CrazyPoly get used, whether a release makes something worse, and where new players are getting stuck. It is deliberately built so that it cannot be tied to you.

**A short, fixed list of events, and no more:** the app being opened; a game starting or ending, and whether it was played alone, on the same device, over local Wi-Fi, or over the internet; a purchase completing; and, for each of the three ways into a networked game - online matchmaking, opening or joining a private room, and hosting or joining over local Wi-Fi - whether it succeeded and how long it took. Each carries the app version, the platform, the interface language and the current theme. That is the whole list - no board state, no opponents, no room codes, nothing about who else was at the table.

**What identifies them is not you.** Each installation generates a random identifier for itself the first time it runs — sixteen random bytes, made on your device, meaningful nowhere else. It is not your account id, not your Google account, not your display name, and not a device or advertising identifier, and it is deliberately kept apart from your account so that the two cannot be joined up. Reinstalling the game produces a new one. No board state, no player names and no reactions are ever included.

**Where it goes.** To **PostHog**, on their European hosting, acting as our processor. Nothing is sent until you have accepted this policy, and nothing is sent from a development build.

**There is no separate switch for this,** the way there is for advertising: accepting this policy is what covers it, the same as it covers everything else described here. We chose not to add one because there is nothing in an installation identifier for a switch to protect — nobody, including us, can trace it back to you, hold it against your account, or connect it to anything else we know about you. §12 still applies: you may object to this processing on the same terms as any other legitimate-interest processing described in this policy, though we have no way to find and remove one installation's past events specifically, for the same reason there was nothing to identify you by in the first place.

---

## 7. Children and families

CrazyPoly is a board game that children play, and we have built it to be safe for them:

* **There is no free-text chat.** Players communicate with a fixed set of emoji reactions, which travel as a number rather than as text. There is no way for a stranger to send a child a written message through CrazyPoly.
* **The whole single-player and local-Wi-Fi game works with no account.**
* **The Android version shows advertisements** (§6.9), and this is the part parents should read closely. One kind is only ever shown when a player asks for it in exchange for a coin; the other only when leaving a match that has ended. **Buying "Remove Ads" turns both off permanently**, and is the option we would point a parent to. There is no advertising at all in the desktop or browser versions.
* **Advertisements are capped at the "G" content rating** — suitable for all audiences — because the game is rated 3+ (§6.9).
* **Personalised advertising can be declined, and then is not used.** In the EEA and the UK the consent form appears before any personalised ad is requested; decline it and ads are still shown but are chosen without a profile of the player. **We do no behavioural profiling of our own and no cross-app tracking**, and we never pass anything about a player to an advertiser ourselves.
* **Usage counting cannot single out a child, or anybody else.** What it collects (§6.10) is anonymous by design, with nothing in it that could identify a person, child or adult.

**A parent or guardian must give permission before a child creates an account, adds friends, or makes a purchase.** Where the law requires verifiable parental consent — the US Children's Online Privacy Protection Act (COPPA) for children under 13, and Article 8 GDPR for children under 16 in the EEA (the age varies by country, from 13 to 16) — that consent must be given by the parent or guardian, and the parent or guardian is the person who agrees to our Terms on the child's behalf.

We do not knowingly collect more from a child than is described in this policy, and none of it is used for advertising or profiling.

**Parents:** write to **support@neathippo.com** and we will tell you what is held on your child's account, correct it, or delete it and the account outright. If you would rather your child used CrazyPoly with no data at all, have them play offline or over local Wi-Fi, where no account is involved.

If we learn that a child's account was created without the parental consent the law requires, we will delete it.

---

## 8. Legal bases (EEA and UK players)

| What | Basis under GDPR |
| --- | --- |
| Running your account, matches, coins, purchases and friends list | Performance of a contract (Art. 6(1)(b)) |
| Keeping the service secure, preventing cheating and abuse, diagnosing faults — including the starting-coins marker in §6.8 | Legitimate interests (Art. 6(1)(f)) |
| Confirming your e-mail address and resetting passwords | Contract, and our legitimate interest in account security |
| Keeping purchase and tax records | Legal obligation (Art. 6(1)(c)) |
| Showing personalised advertisements, and the device access and device identification advertising needs, including identification by IP address (§6.9) | Consent (Art. 6(1)(a)), given or refused through the consent form; withdrawable there or by buying Remove Ads |
| Showing non-personalised advertisements to fund a free game (§6.9) | Legitimate interests (Art. 6(1)(f)), where consent to personalisation was not given |
| Counting anonymous usage events, to improve the game (§6.10) | Legitimate interests (Art. 6(1)(f)) — proportionate because nothing collected can identify you |
| A child's account, where consent is required | Consent of the holder of parental responsibility (Art. 6(1)(a), Art. 8) |

Under Ukrainian law we process personal data on the equivalent grounds set out in the Law of Ukraine "On Personal Data Protection" No. 2297-VI.

---

## 9. Who else touches your data

We use a small number of service providers, and only as processors acting on our instructions. We do not sell personal data, and we do not share it for anyone else's marketing.

| Provider | What they do | What they see |
| --- | --- | --- |
| **Heroic Labs** (Heroic Cloud / Nakama) | Hosts the game server and its database | Everything in §5 — it is the database that holds it |
| **Brevo** (Sendinblue) | Sends confirmation and password-reset e-mails | Your e-mail address and the contents of that message |
| **Google** (Play Billing, Google Sign-In, Play distribution) | Sells and delivers in-app purchases; provides sign-in; distributes the Android app | Your purchase and payment details, which Google handles under its own privacy policy; the sign-in token exchange |
| **PostHog** (EU hosting) | Stores the anonymous usage events in §6.10 | The events listed there, the installation's random identifier, app version, platform, language and theme — nothing that names you |

**Google AdMob is different, and we say so plainly.** For advertising (§6.9), Google does not act only on our instructions: it is an **independent controller** of the data it collects to select and measure ads, under its own privacy policy. We do not receive that data, and we cannot delete it for you — Google's own controls govern it.

We will also disclose data where we are legally required to, or where it is necessary to establish or defend a legal claim or to protect someone's safety.

---

## 10. Where your data goes

Our server and its database are hosted on Heroic Cloud, our e-mail provider operates in the EU, and the anonymous usage events in §6.10 are held on PostHog's European hosting. Data may therefore be processed in the European Union, in the United States and in Ukraine. Where personal data leaves the EEA or the UK, the transfer relies on the European Commission's Standard Contractual Clauses or an adequacy decision, as applicable.

Advertising is the exception to that sentence: what Google collects for ads (§6.9) travels under Google's own arrangements as an independent controller, not ours.

---

## 11. How long we keep things

* **Account data** — for as long as your account exists, and until you delete it (or ask us to).
* **Statistics, coins and entitlements** — for the life of the account; these are the point of having one.
* **Purchase records** — for as long as the law requires us to keep financial records, which outlasts the account.
* **The starting-coins marker (§6.8)** — for as long as we run the online service, and deliberately after the account that created it is deleted. A marker that expired would only postpone the loophole it exists to close.
* **Match records** — a relayed match exists only while somebody is in it. An unfinished-match result is kept long enough for the absent player to be told, and is then discarded.
* **Rejoin notes** — 15 minutes.
* **E-mail and password-reset codes** — 15 minutes, or until used.
* **Server logs** — a short operational window, normally no more than 90 days, unless a specific incident requires keeping one longer.
* **A bug-report log you sent us** — until the report is closed.
* **Anonymous usage events (§6.10)** — kept as counts for as long as they are useful for judging a release. They are not attached to your account and are not deleted with it, because there is nothing in them to find you by.
* **Advertising data** — not ours to keep or delete. Google holds what it collects for ads under its own policy and its own retention rules (§6.9).

---

## 12. Your rights

Wherever you live, you may ask us to:

* **tell you what we hold** about you, and give you a copy;
* **correct** anything that is wrong;
* **delete** your account and the data attached to it — or particular data, without closing the account;
* **restrict or object to** processing based on legitimate interests;
* **withdraw consent** where processing rests on it, without affecting what was done before;
* **receive your data in a portable form**.

**One of these you can exercise yourself, without asking us.** Advertising consent is changed through the consent form or removed outright by buying Remove Ads (§6.9).

Deletion you can carry out yourself too, and it is the fastest way: **User Account → Delete account** in the game deletes the account and everything on our servers attached to it, straight away and with no request to make of us. For any of the others — or for deletion when you cannot get into the account at all — e-mail **support@neathippo.com** from the address on your account, or — for a device-only account — from the device, telling us the display name so we can find it. We will answer within 30 days.

**You do not have to delete your account to have data removed.** Write to **support@neathippo.com** and ask us to delete particular things — your statistics, your friends list, the record of your finished matches — and we will delete them and leave the account itself in place. Your friends list you can also prune yourself, one name at a time, in **Friends**: removing somebody deletes that friendship on our servers rather than hiding it. A few things cannot be separated from the account, and we would rather say so here than in a reply to your request: the e-mail address you sign in with, which *is* the account and can only go when it does; purchase records we are required to keep (§11); and the marker in §6.8, which names a device rather than you. The anonymous usage events in §6.10 are a fourth, for the opposite reason — there is nothing in them that points at you, so there is nothing in them for us to find and remove.

Three honest caveats. First, deletion is genuinely permanent: coins, statistics and the record of which themes the account paid for go with it, and a purchase already made cannot be un-made by us — a theme already unlocked on a device stays unlocked there, and one bought through Google Play stays yours on your Google account, but neither can be restored to a new CrazyPoly account. Second, a **device-only account has no way for us to verify that you are its owner** beyond the request coming from the device itself, so we will ask you to confirm details only its owner would know. Third, one thing outlives the deletion on purpose: the marker described in §6.8, recording that the device you signed up from has already been given the free starting coins. It names a device rather than you, and it is what stops a new account on the same device collecting them again.

**Complaints.** If you are in the EEA or the UK you may complain to your local data protection authority. In Ukraine, the supervisory authority is the Ukrainian Parliament Commissioner for Human Rights (Ombudsman). We would rather you wrote to us first.

---

## 13. Security

Passwords are stored only as salted hashes. Sessions use tokens that expire and that signing out erases from your device. Traffic to the server is encrypted in transit. Confirmation codes are short-lived, rate-limited, and cannot be read out of storage by the account they belong to. Coin balances and entitlements are moved only by the server, never by the game on your device.

None of that is a promise that nothing can ever go wrong. If a breach affects your personal data and the law requires us to tell you, we will.

---

## 14. Changes to this policy

If we change what we collect or what we do with it, we will update this policy, change the effective date at the top, and — where the change is significant — ask you to look at it again in the game before you carry on playing.

---

## 15. Contact

**support@neathippo.com**

Dmytro Korchynskyi, trading as NeatHippo, Ukraine. Write to the address above about anything in this policy — it reaches the person responsible for it. Our postal address is in §1 of the Terms and Conditions.
