import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_tejarat_t_logo(size=512):
    scale = 4
    W = size * scale
    H = size * scale
    
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 1. Background Rounded Squircle with deep rich Emerald Gradient
    bg_pad = 24 * scale
    radius = 120 * scale
    
    c_dark = (4, 47, 36)      # #042F24 Deepest Forest Emerald
    c_mid = (4, 120, 87)      # #047857 Rich Emerald
    c_bright = (16, 185, 129) # #10B981 Mint Emerald
    c_gold = (245, 158, 11)   # #F59E0B Vibrant Gold
    c_gold_light = (254, 240, 138) # #FEF08A Pale Gold
    c_gold_dark = (180, 83, 9)     # #B45309 Amber Dark
    
    # Gradient canvas
    gradient = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(gradient)
    for y in range(int(bg_pad), int(H - bg_pad)):
        t = (y - bg_pad) / (H - 2 * bg_pad)
        # 3-stop gradient
        if t < 0.5:
            ratio = t / 0.5
            r = int(c_bright[0] * (1 - ratio) + c_mid[0] * ratio)
            g = int(c_bright[1] * (1 - ratio) + c_mid[1] * ratio)
            b = int(c_bright[2] * (1 - ratio) + c_mid[2] * ratio)
        else:
            ratio = (t - 0.5) / 0.5
            r = int(c_mid[0] * (1 - ratio) + c_dark[0] * ratio)
            g = int(c_mid[1] * (1 - ratio) + c_dark[1] * ratio)
            b = int(c_mid[2] * (1 - ratio) + c_dark[2] * ratio)
        g_draw.line([(bg_pad, y), (W - bg_pad, y)], fill=(r, g, b, 255), width=1)
        
    # Mask to squircle
    mask = Image.new('L', (W, H), 0)
    m_draw = ImageDraw.Draw(mask)
    m_draw.rounded_rectangle([bg_pad, bg_pad, W - bg_pad, H - bg_pad], radius=radius, fill=255)
    
    # Outer drop shadow
    shadow_mask = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_mask)
    s_draw.rounded_rectangle([bg_pad, bg_pad + 16*scale, W - bg_pad, H - bg_pad + 16*scale], radius=radius, fill=(0, 0, 0, 85))
    shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(radius=16*scale))
    
    img.paste(shadow_mask, (0, 0), shadow_mask)
    img.paste(gradient, (0, 0), mask)
    
    # Double Luxury Gold Trimming
    draw.rounded_rectangle([bg_pad, bg_pad, W - bg_pad, H - bg_pad], radius=radius, outline=c_gold, width=int(6*scale))
    draw.rounded_rectangle([bg_pad + 8*scale, bg_pad + 8*scale, W - bg_pad - 8*scale, H - bg_pad - 8*scale], radius=radius - 8*scale, outline=(255, 255, 255, 70), width=int(2*scale))
    
    # Ambient Light Reflection (Curved shine)
    gloss = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    gloss_draw.ellipse([bg_pad - 40*scale, bg_pad - 120*scale, W - bg_pad + 40*scale, bg_pad + 180*scale], fill=(255, 255, 255, 35))
    img.paste(gloss, (0, 0), mask)
    
    # 2. Central Emblem: Modern Shopping Shield with Bold 3D "T" and Tejarat Urdu
    cx = W // 2
    cy = int(215 * scale)
    
    # Shield / Circle base in center
    shield_r = 145 * scale
    draw.ellipse([cx - shield_r, cy - shield_r, cx + shield_r, cy + shield_r], fill=(255, 255, 255, 245), outline=c_gold, width=int(7*scale))
    draw.ellipse([cx - shield_r + 8*scale, cy - shield_r + 8*scale, cx + shield_r - 8*scale, cy + shield_r - 8*scale], outline=(4, 120, 87, 80), width=int(2*scale))
    
    # Bold, Sculpted "T" Letter (Emerald & Gold 3D styling)
    # Dimensions of T
    bar_w = 190 * scale      # Top bar width
    bar_h = 38 * scale       # Top bar height
    stem_w = 42 * scale      # Vertical stem width
    stem_h = 130 * scale     # Vertical stem height
    
    t_top = cy - 88 * scale
    t_left = cx - bar_w // 2
    
    # T Drop Shadow
    shadow_offset = 6 * scale
    # Top bar shadow
    draw.rounded_rectangle([t_left + shadow_offset, t_top + shadow_offset, t_left + bar_w + shadow_offset, t_top + bar_h + shadow_offset], radius=10*scale, fill=(2, 44, 34, 90))
    # Stem shadow
    draw.rounded_rectangle([cx - stem_w//2 + shadow_offset, t_top + bar_h - 4*scale + shadow_offset, cx + stem_w//2 + shadow_offset, t_top + bar_h + stem_h + shadow_offset], radius=10*scale, fill=(2, 44, 34, 90))
    
    # Top bar of "T" (Emerald green with bevel corners)
    draw.rounded_rectangle([t_left, t_top, t_left + bar_w, t_top + bar_h], radius=10*scale, fill=c_mid)
    # Top bar golden highlight on top edge
    draw.line([(t_left + 10*scale, t_top + 4*scale), (t_left + bar_w - 10*scale, t_top + 4*scale)], fill=c_gold_light, width=int(3*scale))
    
    # Vertical stem of "T"
    draw.rounded_rectangle([cx - stem_w//2, t_top + bar_h - 6*scale, cx + stem_w//2, t_top + bar_h + stem_h], radius=10*scale, fill=c_mid)
    
    # Accent curve at the base of the T (Smiling upward reseller profit curve)
    curve_w = 100 * scale
    curve_h = 30 * scale
    curve_y = t_top + bar_h + stem_h - 18 * scale
    draw.arc([cx - curve_w//2, curve_y, cx + curve_w//2, curve_y + curve_h], start=20, end=160, fill=c_gold, width=int(7*scale))
    
    # Twin Golden Stars / Diamonds on the shoulders of the "T"
    def draw_star(center_x, center_y, d_size):
        pts = [
            (center_x, center_y - d_size),
            (center_x + d_size*0.35, center_y - d_size*0.35),
            (center_x + d_size, center_y),
            (center_x + d_size*0.35, center_y + d_size*0.35),
            (center_x, center_y + d_size),
            (center_x - d_size*0.35, center_y + d_size*0.35),
            (center_x - d_size, center_y),
            (center_x - d_size*0.35, center_y - d_size*0.35)
        ]
        draw.polygon(pts, fill=c_gold, outline=c_gold_dark)
        
    draw_star(t_left + 18*scale, t_top - 18*scale, 16*scale)
    draw_star(t_left + bar_w - 18*scale, t_top - 18*scale, 16*scale)
    draw_star(cx, t_top - 24*scale, 20*scale)
    
    # 3. Typography: "TEJARAT" & "تجارت"
    try:
        font_path = "C:/Windows/Fonts/arialbd.ttf"
        if not os.path.exists(font_path):
            font_path = "C:/Windows/Fonts/segoeuib.ttf"
        font_urdu_path = "C:/Windows/Fonts/arial.ttf"
        
        font_tejarat = ImageFont.truetype(font_path, int(46 * scale))
        font_urdu = ImageFont.truetype(font_urdu_path, int(26 * scale))
        font_sub = ImageFont.truetype(font_path, int(15 * scale))
    except Exception:
        font_tejarat = ImageFont.load_default()
        font_urdu = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        
    # Text "TEJARAT"
    title = "TEJARAT"
    bbox = draw.textbbox((0, 0), title, font=font_tejarat)
    tw = bbox[2] - bbox[0]
    tx = (W - tw) // 2
    ty = int(390 * scale)
    
    # Text shadow
    draw.text((tx, ty + 2*scale), title, font=font_tejarat, fill=(0, 30, 20, 220))
    # Text main
    draw.text((tx, ty), title, font=font_tejarat, fill=(255, 255, 255, 255))
    
    # Subtitle Badge: "تجارت · RESELLER PLATFORM"
    badge_text = "تجارت · RESELLER APP"
    s_bbox = draw.textbbox((0, 0), badge_text, font=font_sub)
    sw = s_bbox[2] - s_bbox[0]
    sx = (W - sw) // 2
    sy = int(ty + (bbox[3] - bbox[1]) + 14 * scale)
    
    badge_pad_x = 18 * scale
    badge_pad_y = 5 * scale
    draw.rounded_rectangle(
        [sx - badge_pad_x, sy - badge_pad_y, sx + sw + badge_pad_x, sy + (s_bbox[3] - s_bbox[1]) + badge_pad_y],
        radius=9*scale,
        fill=c_gold
    )
    draw.text((sx, sy), badge_text, font=font_sub, fill=(15, 30, 20, 255))
    
    # Downsample with Lanczos
    return img.resize((size, size), Image.Resampling.LANCZOS)

# Create and save
logo_img = create_tejarat_t_logo(512)
logo_img.save("markaz_assets/tejarat_logo.png")
logo_img.save("tejarat_logo.png")
print("Saved markaz_assets/tejarat_logo.png and tejarat_logo.png (512x512) with prominent 'T'!")

# Update launcher icons
targets = [
    ("android_source/res/drawable/ic_launcher.png", 192),
    ("android_source/res/mipmap-mdpi/ic_launcher.png", 48),
    ("android_source/res/mipmap-hdpi/ic_launcher.png", 72),
    ("android_source/res/mipmap-xhdpi/ic_launcher.png", 96),
    ("android_source/res/mipmap-xxhdpi/ic_launcher.png", 144),
    ("android_source/res/mipmap-xxxhdpi/ic_launcher.png", 192),
    ("web_ota_app/tejarat_logo.png", 512),
    ("web_ota_app/markaz_assets/tejarat_logo.png", 512),
    ("android_source/assets/tejarat_logo.png", 512),
    ("android_source/assets/markaz_assets/tejarat_logo.png", 512),
]

for p, sz in targets:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    icon = logo_img.resize((sz, sz), Image.Resampling.LANCZOS)
    icon.save(p)
    print(f"Updated {p} ({sz}x{sz})")

print("All logo icons updated with the stylish 'T' design successfully!")
