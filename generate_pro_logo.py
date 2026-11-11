import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_super_pro_logo(size=512):
    scale = 4
    W = size * scale
    H = size * scale
    
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 1. Background Squircle with rich vibrant Emerald Gradient
    pad = 20 * scale
    radius = 115 * scale
    
    c_dark = (3, 41, 31)       # #03291F Deep Luxury Emerald
    c_emerald = (4, 120, 87)   # #047857 Rich Emerald Green
    c_mint = (16, 185, 129)    # #10B981 Radiant Mint
    c_gold = (245, 158, 11)    # #F59E0B Rich Amber Gold
    c_gold_light = (253, 230, 138) # Pale Gold highlight
    c_gold_dark = (180, 83, 9) # Amber bronze
    
    # Gradient background
    gradient = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(gradient)
    for y in range(int(pad), int(H - pad)):
        t = (y - pad) / (H - 2 * pad)
        if t < 0.45:
            ratio = t / 0.45
            r = int(c_mint[0] * (1 - ratio) + c_emerald[0] * ratio)
            g = int(c_mint[1] * (1 - ratio) + c_emerald[1] * ratio)
            b = int(c_mint[2] * (1 - ratio) + c_emerald[2] * ratio)
        else:
            ratio = (t - 0.45) / 0.55
            r = int(c_emerald[0] * (1 - ratio) + c_dark[0] * ratio)
            g = int(c_emerald[1] * (1 - ratio) + c_dark[1] * ratio)
            b = int(c_emerald[2] * (1 - ratio) + c_dark[2] * ratio)
        g_draw.line([(pad, y), (W - pad, y)], fill=(r, g, b, 255), width=1)
        
    mask = Image.new('L', (W, H), 0)
    m_draw = ImageDraw.Draw(mask)
    m_draw.rounded_rectangle([pad, pad, W - pad, H - pad], radius=radius, fill=255)
    
    # Soft drop shadow
    shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([pad, pad + 14*scale, W - pad, H - pad + 14*scale], radius=radius, fill=(0, 0, 0, 95))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=15*scale))
    
    img.paste(shadow, (0, 0), shadow)
    img.paste(gradient, (0, 0), mask)
    
    # Outer Luxury Gold Trimming
    draw.rounded_rectangle([pad, pad, W - pad, H - pad], radius=radius, outline=c_gold, width=int(7*scale))
    draw.rounded_rectangle([pad + 7*scale, pad + 7*scale, W - pad - 7*scale, H - pad - 7*scale], radius=radius - 7*scale, outline=(255, 255, 255, 80), width=int(2*scale))
    
    # Top curved ambient shine
    shine = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    shine_draw = ImageDraw.Draw(shine)
    shine_draw.ellipse([pad - 20*scale, pad - 100*scale, W - pad + 20*scale, pad + 190*scale], fill=(255, 255, 255, 40))
    img.paste(shine, (0, 0), mask)
    
    # 2. Central White/Gold Luxury Emblem Shield
    cx = W // 2
    cy = int(210 * scale)
    shield_r = 142 * scale
    
    # White circular plaque
    draw.ellipse([cx - shield_r, cy - shield_r, cx + shield_r, cy + shield_r], fill=(255, 255, 255, 255), outline=c_gold, width=int(8*scale))
    draw.ellipse([cx - shield_r + 9*scale, cy - shield_r + 9*scale, cx + shield_r - 9*scale, cy + shield_r - 9*scale], outline=(4, 120, 87, 60), width=int(3*scale))
    
    # 3. Super Bold, Iconic 3D "T" Emblem
    # Top bar
    bar_w = 186 * scale
    bar_h = 36 * scale
    stem_w = 44 * scale
    stem_h = 135 * scale
    
    t_top = cy - 85 * scale
    t_left = cx - bar_w // 2
    
    # Drop shadow of T
    so = 7 * scale
    draw.rounded_rectangle([t_left + so, t_top + so, t_left + bar_w + so, t_top + bar_h + so], radius=10*scale, fill=(2, 40, 28, 90))
    draw.rounded_rectangle([cx - stem_w//2 + so, t_top + bar_h - 4*scale + so, cx + stem_w//2 + so, t_top + bar_h + stem_h + so], radius=10*scale, fill=(2, 40, 28, 90))
    
    # Top bar: Emerald green with golden accent bevel
    draw.rounded_rectangle([t_left, t_top, t_left + bar_w, t_top + bar_h], radius=10*scale, fill=c_emerald)
    # Gold highlight line on top edge of T
    draw.line([(t_left + 8*scale, t_top + 4*scale), (t_left + bar_w - 8*scale, t_top + 4*scale)], fill=c_gold_light, width=int(3*scale))
    
    # Vertical stem of T
    draw.rounded_rectangle([cx - stem_w//2, t_top + bar_h - 6*scale, cx + stem_w//2, t_top + bar_h + stem_h], radius=10*scale, fill=c_emerald)
    
    # Golden upward profit arrow / dynamic curve inside the stem
    arrow_w = 26 * scale
    arrow_y = t_top + bar_h + 30 * scale
    # Chevron profit arrow
    pts = [
        (cx, arrow_y),
        (cx + arrow_w, arrow_y + 24*scale),
        (cx + arrow_w*0.5, arrow_y + 24*scale),
        (cx, arrow_y + 12*scale),
        (cx - arrow_w*0.5, arrow_y + 24*scale),
        (cx - arrow_w, arrow_y + 24*scale),
    ]
    draw.polygon(pts, fill=c_gold_light, outline=c_gold_dark)
    
    # Golden smile base curve below T
    draw.arc([cx - 50*scale, t_top + bar_h + stem_h - 22*scale, cx + 50*scale, t_top + bar_h + stem_h + 8*scale], start=20, end=160, fill=c_gold, width=int(8*scale))
    
    # Stars on the shoulders of the T
    def draw_star(center_x, center_y, size):
        pts = []
        for i in range(8):
            angle = i * math.pi / 4
            r = size if i % 2 == 0 else size * 0.4
            pts.append((center_x + r * math.cos(angle), center_y + r * math.sin(angle)))
        draw.polygon(pts, fill=c_gold, outline=c_gold_dark)
        
    draw_star(t_left + 18*scale, t_top - 20*scale, 16*scale)
    draw_star(t_left + bar_w - 18*scale, t_top - 20*scale, 16*scale)
    draw_star(cx, t_top - 28*scale, 20*scale)
    
    # 4. Bold Typography: "TEJARAT" + "تجارت"
    try:
        font_path = "C:/Windows/Fonts/arialbd.ttf"
        if not os.path.exists(font_path):
            font_path = "C:/Windows/Fonts/segoeuib.ttf"
        font_main = ImageFont.truetype(font_path, int(46 * scale))
        font_sub = ImageFont.truetype(font_path, int(15 * scale))
    except Exception:
        font_main = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        
    title = "TEJARAT"
    bbox = draw.textbbox((0, 0), title, font=font_main)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (W - tw) // 2
    ty = int(388 * scale)
    
    # Drop shadow
    draw.text((tx, ty + 2*scale), title, font=font_main, fill=(0, 30, 20, 230))
    draw.text((tx, ty), title, font=font_main, fill=(255, 255, 255, 255))
    
    # Subtitle Badge: "تجارت · RESELLER PLATFORM"
    sub_text = "تجارت · RESELLER APP"
    sbox = draw.textbbox((0, 0), sub_text, font=font_sub)
    sw = sbox[2] - sbox[0]
    sx = (W - sw) // 2
    sy = int(ty + th + 14 * scale)
    
    # Pill badge
    bx = 18 * scale
    by = 5 * scale
    draw.rounded_rectangle([sx - bx, sy - by, sx + sw + bx, sy + (sbox[3] - sbox[1]) + by], radius=9*scale, fill=c_gold)
    draw.text((sx, sy), sub_text, font=font_sub, fill=(15, 30, 20, 255))
    
    # Circular version for Android roundIcon
    round_img = img.copy()
    round_mask = Image.new('L', (W, H), 0)
    rm_draw = ImageDraw.Draw(round_mask)
    rm_draw.ellipse([pad, pad, W - pad, H - pad], fill=255)
    
    round_output = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    round_output.paste(img, (0, 0), round_mask)
    # Circle gold border
    ro_draw = ImageDraw.Draw(round_output)
    ro_draw.ellipse([pad, pad, W - pad, H - pad], outline=c_gold, width=int(7*scale))
    
    final_squircle = img.resize((size, size), Image.Resampling.LANCZOS)
    final_round = round_output.resize((size, size), Image.Resampling.LANCZOS)
    
    return final_squircle, final_round

squircle_logo, round_logo = create_super_pro_logo(512)

# Save master logos
os.makedirs("markaz_assets", exist_ok=True)
squircle_logo.save("markaz_assets/tejarat_logo.png")
squircle_logo.save("tejarat_logo.png")
round_logo.save("markaz_assets/tejarat_logo_round.png")

# All Android launcher target directories
targets = [
    ("android_source/res/drawable/ic_launcher.png", 192, squircle_logo),
    ("android_source/res/drawable/ic_launcher_round.png", 192, round_logo),
    ("android_source/res/mipmap-mdpi/ic_launcher.png", 48, squircle_logo),
    ("android_source/res/mipmap-mdpi/ic_launcher_round.png", 48, round_logo),
    ("android_source/res/mipmap-hdpi/ic_launcher.png", 72, squircle_logo),
    ("android_source/res/mipmap-hdpi/ic_launcher_round.png", 72, round_logo),
    ("android_source/res/mipmap-xhdpi/ic_launcher.png", 96, squircle_logo),
    ("android_source/res/mipmap-xhdpi/ic_launcher_round.png", 96, round_logo),
    ("android_source/res/mipmap-xxhdpi/ic_launcher.png", 144, squircle_logo),
    ("android_source/res/mipmap-xxhdpi/ic_launcher_round.png", 144, round_logo),
    ("android_source/res/mipmap-xxxhdpi/ic_launcher.png", 192, squircle_logo),
    ("android_source/res/mipmap-xxxhdpi/ic_launcher_round.png", 192, round_logo),
    ("web_ota_app/tejarat_logo.png", 512, squircle_logo),
    ("web_ota_app/markaz_assets/tejarat_logo.png", 512, squircle_logo),
    ("android_source/assets/tejarat_logo.png", 512, squircle_logo),
    ("android_source/assets/markaz_assets/tejarat_logo.png", 512, squircle_logo)
]

for path, sz, source_img in targets:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    res = source_img.resize((sz, sz), Image.Resampling.LANCZOS)
    res.save(path)
    print(f"Generated {path} ({sz}x{sz})")

print("All new launcher icons and logos created successfully!")
