#!/usr/bin/env python3
"""Generate ORIGINAL, diverse character cards by composite sampling (no real people).
  python roster_gen.py --n 8 --female-ratio 0.75 --seed 7 [--aesthetic "F1 paddock glam"]"""
import argparse, random, json
HERITAGE = ["West African", "East African", "Afro-Caribbean", "North African", "Punjabi", "Tamil", "Korean", "Japanese", "Han Chinese",
            "Vietnamese", "Malay", "Thai", "Filipina", "Peranakan", "Middle Eastern", "Brazilian", "Mexican", "Mediterranean",
            "Northern European", "Pacific Islander", "mixed heritage"]
AGES = ["25-29", "30-34", "35-39", "40-49", "50-60"]
F_BUILD = ["sprinter", "glute/fitness athlete", "pilates/dancer", "swimmer", "tennis/golf", "boxer", "runway editorial", "curvy confident", "girl-next-door", "corporate chic", "street-style", "mature elegance"]
M_BUILD = ["sprinter", "rugby powerhouse", "footballer", "F1-driver build", "boxer", "swimmer", "runway editorial", "bearded rugged", "relatable dad-bod", "silver fox", "corporate sharp", "street-style"]
AESTHETIC = ["WAG matchday glam", "F1 paddock glam", "Riviera old-money", "courtside glam", "tennis-whites club", "runway editorial", "fitness-influencer",
             "beach-villa reality-TV", "K-pop idol", "Bollywood glam", "Lagos owambe glam", "clean girl", "Scandi minimal", "Y2K"]
FACE = {"face": ["oval", "heart", "square", "diamond", "long", "round"], "cheekbones": ["high", "soft", "sculpted"], "jaw": ["defined", "soft", "tapered"],
        "eyes": ["almond", "hooded", "deep-set", "monolid", "upturned", "wide-set"], "brows": ["straight", "arched", "full", "feathered"],
        "nose": ["straight", "button", "aquiline", "broad", "upturned"], "lips": ["full", "bow-shaped", "wide", "defined"],
        "mark": ["dimples", "gap tooth", "freckles", "beauty mark", "none", "subtle scar"]}
HAIR = ["straight sleek", "loose waves", "3b curls", "3c curls", "4b coils", "4c coils", "locs", "box braids", "cornrows", "twists", "pixie cut", "silver bob", "buzz cut", "slicked back"]
VOICE = ["Lagos English", "London RP", "London MLE", "Manchester", "Southern US", "NYC", "California", "light Singlish", "Malaysian English", "Australian",
         "South African", "Indian English", "French-accented English", "Brazilian-accented English", "Korean-accented English"]
CLASS = ["old money", "new money", "comfortable middle", "squeezed middle", "working poor", "first-gen climber"]
WOUND = ["fear of being used", "fear of losing it all", "fear of being seen as shallow", "fear of letting family down", "fear of never catching up", "fear of being exposed as a fraud"]
TRAITS = ["confident", "playful", "warm", "witty", "fierce", "calm", "driven", "cheeky", "elegant", "grounded", "chaotic-good", "mysterious"]
def main():
    a = argparse.ArgumentParser(); a.add_argument("--n", type=int, default=8); a.add_argument("--female-ratio", type=float, default=0.75)
    a.add_argument("--seed", type=int, default=7); a.add_argument("--aesthetic"); args = a.parse_args(); r = random.Random(args.seed)
    nf = round(args.n * args.female_ratio); her = r.sample(HERITAGE, min(args.n, len(HERITAGE)))  # no repeated heritage
    ages = (AGES * 3)[:args.n]; r.shuffle(ages); cards = []
    for i in range(args.n):
        female = i < nf; build = r.choice(F_BUILD if female else M_BUILD)
        if build in ("mature elegance", "silver fox"): ages[i] = r.choice(["40-49", "50-60"])
        feats = {k: r.choice(v) for k, v in FACE.items()}
        cards.append({"handle": f"@{'LEAD' if female else 'SUPPORT'}_{i+1:02d}", "gender": "female" if female else "male", "age_band": ages[i],
                      "heritage": her[i % len(her)], "build": build, "aesthetic": args.aesthetic or r.choice(AESTHETIC), "face": feats,
                      "hair": r.choice(HAIR), "voice": r.choice(VOICE), "personality": r.sample(TRAITS, 3), "class_background": r.choice(CLASS), "money_wound": r.choice(WOUND),
                      "rules": "original person; no real names/logos in prompts; lookalike QC; adult"})
    print(json.dumps(cards, indent=2, ensure_ascii=False))
if __name__ == "__main__": main()
