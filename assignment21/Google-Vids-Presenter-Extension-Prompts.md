# Google Vids Presenter Continuity and Extension Prompts

> **Reference only:** Use [Google-Vids-Story-Scene-Prompts.md](Google-Vids-Story-Scene-Prompts.md) for the current build. This file was written before the correct colorful flat-cloth product reference was provided.

## Current Clip

The example clip shows a stylish Asian woman speaking to camera while holding a product image. Keep this presenter as a brief host or presenter cameo in the advertisement if she fits the final creative direction. She does not need to appear in every scene.

The screenshot shows a 10-second, 720p clip and the Google Vids controls `Insert`, `Extend`, `Upscale`, and `Recreate`. The blue notice says the monthly generation limit has been reached, so new generation may remain unavailable until the displayed reset time.

## Recommended Production Plan

Create the actual 60-70 second Swedish dishcloth advertisement in the other Google Vids account with the larger generation limit. Use several connected short scenes rather than asking the generator for one uninterrupted 60-second clip.

Use the woman for one strong presenter scene, preferably after the opening problem scene:

1. Open with a quick coffee ring, crumbs, or sink splash.
2. Cut to the woman holding the actual reusable dishcloth or the correct product reference.
3. Let her deliver one clear product line.
4. Cut to hands demonstrating wet, wring, wipe, rinse, and dry.
5. Finish with the real logo, product image, and call to action added in the editor.

This gives the ad a human moment without making the whole video depend on perfect face continuity. If Google Vids keeps her appearance consistent from a reference image, she can appear in a second scene. Otherwise, use her once and let the product demonstrations carry the rest.

## What To Do In Google Vids

1. In the example account, click `Insert` if you want to save the woman clip for reference or export it as a short cameo.
2. Do not repeatedly click `Extend` or `Recreate` while the limit notice is active. They may fail and will not improve the existing clip.
3. When the limit resets, select the inserted clip and click `Extend`.
4. In the larger-limit account, paste the main 60-70 second project prompt from `Google-Vids-Continuity-Prompts.md`.
5. Repeat the process for the next sections, checking that the presenter, outfit, product, kitchen, and lighting remain consistent.
6. Add the real Your Product logo and final text manually in the editor. Do not ask the generator to create a readable logo or brand text inside the footage.

`Insert` saves the clip to the timeline. `Extend` creates a continuation from the selected generated clip. `Recreate` makes a new variation and may change the presenter, product, or setting. `Upscale` is optional and is not needed for the first draft.

## Presenter Cameo Prompt For The Larger-Limit Account

Upload a clear frame or image reference of the woman if Google Vids allows it, and upload the actual Your Product dishcloth image as a separate product reference. Then use this prompt for one short scene:

> Create one 7-10 second vertical 9:16 presenter scene for the same Your Product Reusable Swedish Dishcloth 10-Pack advertisement. Use the uploaded woman as the presenter reference: keep her same face, long dark hair, cream knit sweater, friendly expression, and natural speaking style. Show her in a bright practical kitchen holding the actual reusable Swedish dishcloth product reference, not a black cylinder or unrelated object. She looks at the camera and says: “For the little kitchen messes that happen every day, keep a reusable cloth ready. Wet, wring, and wipe.” Keep soft natural daylight, realistic commercial style, and gentle camera movement. This is one short insert inside a longer advertisement. Do not create readable text, labels, logos, invented packaging, statistics, discounts, or extra people.

If the generated woman does not match the reference closely, keep the best single version as a cameo and do not regenerate the entire advertisement around her.

## Continuity Lock

Paste this at the beginning of every extension prompt:

> Continue directly from the final frame of the previous clip. Use the exact same presenter: the same adult Asian woman, same face, same long dark hair, same cream knit sweater, same calm friendly delivery, and the same bright practical kitchen. Keep the same camera style, soft natural lighting, product appearance, and vertical portrait framing. Do not introduce another person, a different outfit, a different kitchen, different lighting, new text, a new logo, or a new brand name.

## Extension Prompt 1: Explain The Everyday Problem

> Continue directly from the final frame of the previous clip. Use the exact same presenter and continuity lock. She lowers the product slightly, looks at the camera, and gestures toward a small coffee ring and a few crumbs on the counter. She speaks naturally: “Small kitchen messes are part of every morning. A coffee ring, a few crumbs, or a splash near the sink can make the counter feel unfinished.” Keep the movement natural and realistic. No captions, logos, or readable text inside the generated footage.

## Extension Prompt 2: Show The Product Routine

> Continue directly from the final frame of the previous clip. Use the exact same presenter and continuity lock. She turns toward the counter, picks up the reusable Swedish dishcloth, wets it, gently wrings it out, and wipes the small coffee ring in one smooth motion. She says: “Keep a reusable cloth ready for the quick wipe-down. Wet it, wring it, and wipe.” Make the cloth and hand movement clear. Do not change the product, presenter, kitchen, or outfit. No generated text or logo.

## Extension Prompt 3: Show Several Use Cases

> Continue directly from the final frame of the previous clip. Use the exact same presenter and continuity lock. Show a short practical sequence of the same cloth wiping a kitchen counter, a dining table, and a small sink splash. Keep the presenter’s hands and the same cloth consistent across the sequence. She says: “Use it for everyday kitchen jobs, from the counter and table to the sink area.” Keep the tone helpful and low-pressure. No new people, no location change, and no readable text.

## Extension Prompt 4: Explain The 10-Pack

> Continue directly from the final frame of the previous clip. Use the exact same presenter and continuity lock. She places the cloth beside the sink and shows several matching reusable dishcloths neatly stacked on the counter. She says: “The 10-pack makes it easier to keep fresh cloths ready through a busy week.” Keep the product count visually natural without inventing packaging text, discounts, or claims. No logo or captions generated in the footage.

## Extension Prompt 5: Closing Demonstration

> Continue directly from the final frame of the previous clip. Use the exact same presenter and continuity lock. She rinses the cloth, gently wrings it, and places it open near the sink to dry. She looks back at the camera and says: “Rinse it after use, then let it dry in an open spot.” Keep the scene clean, practical, and realistic. No new person, no different kitchen, and no generated text.

## Final Call To Action

Do this part in the Google Vids editor rather than generating it inside the scene:

```text
YOUR PRODUCT
CLEANER HOME, EASIER LIFE
Reusable Swedish Dishcloth 10-Pack
SHOP NOW
```

Use the real logo file from `assignment13/assets/logo_your_prod.png`. Add the real product image only if it matches the product shown in the video.

## Cleaner Spoken Line For The Existing Prompt

The visible prompt appears to say something like “with this tool we can have our morning cleaning coffee at ease, order now...”. That wording is unclear and sounds like the product is a coffee tool. Replace it with:

> “A simple reusable routine for morning kitchen messes. Wet, wring, wipe, rinse, and dry. Shop the Reusable Swedish Dishcloth 10-Pack.”

## Important Checks

- Keep the presenter. She can be the host for the full ad.
- If the black cylindrical object is not the actual dishcloth product, do not describe it as the product. Use the actual product image or show the cloth in the next scene.
- Use one consistent voice. If the generated voice changes between clips, mute those clips and add one continuous voiceover in the editor.
- Avoid claims such as “best,” “germ-free,” “antibacterial,” “zero waste,” or guaranteed results.
- A 10-second clip can be one scene. Five or six connected clips plus a 4-6 second end card can create a 55-70 second ad.
