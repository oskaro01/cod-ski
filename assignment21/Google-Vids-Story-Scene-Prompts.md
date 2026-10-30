# Google Vids Story Ad: 10-Second Clip Plan

## Important: the current problem

The warning about a video being over the 10-second limit applies to the **source clip selected for Extend**. It does not mean the final Vid must be under 10 seconds.

When a growing timeline or long clip is used as the source, Google Vids keeps only the last 10 seconds and uses that as the next generation input. This can make the continuity unreliable and can waste generations.

For this advertisement, use **Create + Insert for each major scene**. Use Extend only when a single generated clip needs a very short continuation. Do not extend the whole timeline repeatedly.

Google Vids generated clips can be selected between 3 and 10 seconds. The plan below uses five standalone clips, each about 8-10 seconds, followed by a manually created end card. The target is 55-58 seconds, safely below the assignment's 60-second maximum.

## The math

| Part | Planned duration | Running total |
|---|---:|---:|
| Scene 1: presenter hook and problem | 10 sec | 10 sec |
| Scene 2: product reveal and wet/wring | 10 sec | 20 sec |
| Scene 3: wipe and everyday uses | 10 sec | 30 sec |
| Scene 4: 10-pack rotation and drying | 10 sec | 40 sec |
| Scene 5: presenter close and CTA | 10 sec | 50 sec |
| Manual logo end card | 5-8 sec | 55-58 sec |

If a generated clip is only 8 seconds, the total becomes about 45-48 seconds before the end card. That is still usable. Add a short product still, a clean transition, or a little extra end-card time in the editor rather than generating another long extension.

## Reference uploads and labels

Upload these in this order before generating any scene:

1. `C:/Users/ASUS/Downloads/anna.png` -> confirm the interface label, expected to be `@image1`.
2. `C:/Users/ASUS/Downloads/maxresdefault.jpg` -> confirm the interface label, expected to be `@image2`.

If Google Vids displays different labels, replace `@image1` and `@image2` in the prompts with the labels shown in the interface.

The presenter is the same smiling Asian woman with long brown hair, a cream knit sweater, and a warm bright kitchen. The product is the exact reference in `@image2`: flat, thin, textured rectangular Swedish dishcloths in bright colors such as pink, blue, yellow, and green. Never substitute a black cylinder, sponge, bottle, muted stack, or unrelated object.

Use the real logo manually at the end. Do not ask the video generator to create readable logo or packaging text.

## Compact continuity anchor

Use this short wording inside a scene prompt when needed:

> Keep the same realistic commercial style, warm bright kitchen, soft daylight, portrait 9:16 framing, and exact product appearance from @image2. When the presenter appears, use the same woman from @image1 with the same face, long brown hair, cream knit sweater, and friendly expression. Do not add a black cylinder, unrelated product, extra people, generated logo, or readable text.

For demonstration shots, add:

> Use neat adult hands with consistent skin tone and appearance. Avoid old-looking hands, extra fingers, and distorted objects.

## Current five-scene plan

### Scene 1: presenter hook and everyday problem, 0-10 seconds

Use **Create**, not Extend. Set the generated clip duration as close to 10 seconds as the interface allows. Insert it immediately after generation.

> Create one 8-10 second vertical 9:16 product advertisement clip. Use the exact presenter avatar from @image1: the same smiling Asian woman, same long brown hair, same cream knit sweater, and same warm bright kitchen. Use @image2 as the exact product reference. She holds one flat, thin, textured rectangular Swedish dishcloth in a bright color such as pink, blue, yellow, or green. She faces the camera and says naturally: "Every morning, the little kitchen messes show up before the day even begins." Near the end, show a quick cut to a coffee ring and a few breakfast crumbs. Friendly, realistic commercial style. No black cylinder, unrelated item, generated logo, captions, packaging text, or extra people.

### Scene 2: product reveal, wet and wring, 10-20 seconds

Use **Create** as a separate clip. Do not select the complete timeline and press Extend.

> Create one separate 8-10 second vertical 9:16 product demonstration clip in the same warm bright kitchen. Use @image2 as the exact reference for the flat, thin, textured rectangular Swedish dishcloths in bright pink, blue, yellow, and green. Show a clean close-up of one cloth being wetted under the tap and gently wrung once over the sink. Use neat adult hands with consistent appearance and no old-looking hands or extra fingers. Add this natural voiceover: "A reusable cloth is ready for those everyday kitchen wipe-downs." Realistic water movement, soft daylight, practical commercial style. No black cylinder, sponge, bottle, packaging, logo, or readable text.

### Scene 3: wipe and everyday uses, 20-30 seconds

Use **Create** as a separate clip. A few quick cuts inside this one clip are better than making three extra scenes.

> Create one separate 8-10 second vertical 9:16 product demonstration clip. Use the exact Swedish dishcloth from @image2 and the same warm bright kitchen style. Show one matching adult hand using the cloth to wipe crumbs and a coffee ring from a counter, then make two quick clean cuts to a dining table and a small sink splash. Keep the cloth flat, thin, textured, and brightly colored. Add this voiceover: "Use it on the counter, around the table, or beside the sink." Keep the clean-up realistic and natural, with no exaggerated instant effect. No product changes, extra hands, black cylinder, logo, or readable text.

### Scene 4: 10-pack rotation and drying, 30-40 seconds

Use **Create** as a separate clip. This is the replacement for the old Scene 4 onward chain that was causing repeated Extend warnings.

> Create one separate 8-10 second vertical 9:16 product demonstration clip. Show several exact flat, thin, textured Swedish dishcloths from @image2 in bright pink, blue, yellow, and green arranged neatly beside the sink to represent a 10-pack. A matching adult hand picks up one fresh cloth, then rinses the used cloth, gently wrings it, and places it open near the sink to dry. Add this voiceover: "Keep fresh cloths ready through the week, then rinse and let the used one dry open." Keep the kitchen calm and realistic. Do not invent packaging, labels, discounts, certifications, readable text, extra people, or a different product.

### Scene 5: presenter close and CTA, 40-50 seconds

Use **Create** with @image1 again. Do not extend a long timeline to bring the presenter back.

> Create one separate 8-10 second closing presenter clip for the same Your Product advertisement. Use the exact presenter avatar from @image1: same face, long brown hair, cream knit sweater, friendly expression, and warm bright kitchen. Use @image2 as the product reference. She holds one exact flat, thin, textured rectangular Swedish dishcloth in a bright color and looks into the camera. She says naturally: "A simple routine for a cleaner-feeling kitchen. Your Product. Cleaner Home, Easier Life." Keep the realistic warm commercial style. No generated captions, logo, packaging text, extra people, black cylinder, or different product.

## Manual end card, 50-55/58 seconds

Add this manually in Google Vids. Use 5-8 seconds depending on the actual timeline length:

```text
YOUR PRODUCT
CLEANER HOME, EASIER LIFE
Reusable Swedish Dishcloth 10-Pack
SHOP NOW
```

Use the real logo from `assignment13/assets/logo_your_prod.png`. Keep the product image or a clean product still visible if available. Do not generate the logo or readable words with AI.

## Exact workflow from here

1. Keep any good clips already created. Do not delete them just because the old plan had more scenes.
2. Stop using Extend on the full timeline. Do not use a long previous clip as the source for a new generation.
3. For each remaining scene, choose **Create**, add the relevant `@image1` or `@image2` reference, paste only that scene's prompt, and click **Insert** after it renders.
4. Watch the timeline duration after every insertion. The five generated clips should total about 50 seconds if each is 10 seconds.
5. Add the real logo and manual end card. Trim the final result to 55-60 seconds and never export above 60 seconds.
6. Add one consistent voiceover track and manually correct captions after the edit is complete. Mute inconsistent generated speech if necessary.
7. Review the final video for presenter identity, dishcloth shape and colors, hands, product consistency, audio, logo, and CTA.

## When Extend is appropriate

Use Extend only for a single generated clip when you need a small continuation and the selected source itself is no longer than 10 seconds. If Vids displays the warning that only the last 10 seconds will be kept, cancel that extension and return to **Create** for a new standalone scene.

## Claim and production safety

- Do not claim best, germ-free, antibacterial, zero waste, guaranteed results, or certifications unless verified.
- Use only product images or footage that you own or have permission to use.
- Keep all important visual elements inside the vertical safe area.
- Check that the final export is no longer than 60 seconds.
