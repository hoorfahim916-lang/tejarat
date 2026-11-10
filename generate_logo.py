import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_tejarat_logo(size=512):
    # 4x super-sampling for anti-aliased perfection
    scale = 4
    W = size * scale
    H = size * scale
    
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 1. Background Squircle with rich gradient
    bg_pad = 28 * scale
    radius = 110 * scale
    
    # Gradient background
    c_top = (4, 120, 87)       # Emerald #047857
    c_bot = (6, 78, 59)        # Deep Green #064E3B
    c_accent = (16, 185, 129)  # Mint Green #10B981
    c_gold = (245, 158, 11)    # Amber Gold #F59E0B
    c_gold_light = (252, 211, 77) # Soft Gold #FCD34D
    
    # Create gradient layer
    gradient = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(gradient)
    for y in range(int(bg_pad), int(H - bg_pad)):
        t = (y - bg_pad) / (H - 2 * bg_pad)
        r = int(c_top[0] * (1 - t) + c_bot[0] * t)
        g = int(c_top[1] * (1 - t) + c_bot[1] * t)
        b = int(c_top[2] * (1 - t) + c_bot[2] * t)
        g_draw.line([(bg_pad, y), (W - bg_pad, y)], fill=(r, g, b, 255), width=1)
        
    # Mask gradient into rounded rectangle
    mask = Image.new('L', (W, H), 0)
    m_draw = ImageDraw.Draw(mask)
    m_draw.rounded_rectangle([bg_pad, bg_pad, W - bg_pad, H - bg_pad], radius=radius, fill=255)
    
    # Subtle drop shadow behind the squircle
    shadow_mask = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_mask)
    s_draw.rounded_rectangle([bg_pad, bg_pad + 16*scale, W - bg_pad, H - bg_pad + 16*scale], radius=radius, fill=(0, 0, 0, 70))
    shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(radius=14*scale))
    
    img.paste(shadow_mask, (0, 0), shadow_mask)
    img.paste(gradient, (0, 0), mask)
    
    # Gold border on squircle
    draw.rounded_rectangle([bg_pad, bg_pad, W - bg_pad, H - bg_pad], radius=radius, outline=c_gold, width=int(5*scale))
    draw.rounded_rectangle([bg_pad + 6*scale, bg_pad + 6*scale, W - bg_pad - 6*scale, H - bg_pad - 6*scale], radius=radius - 6*scale, outline=(255, 255, 255, 50), width=int(2*scale))
    
    # Top corner ambient gloss / light sweep
    gloss = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    gloss_draw.ellipse([bg_pad, bg_pad - 80*scale, W - bg_pad, bg_pad + 200*scale], fill=(255, 255, 255, 30))
    img.paste(gloss, (0, 0), mask)
    
    # 2. Main Icon: Modern Shopping Bag & Tejarat 'ت' Symbol
    bag_w = 230 * scale
    bag_h = 230 * scale
    bag_x = (W - bag_w) // 2
    bag_y = int(140 * scale)
    
    # Bag Handle (Gold arc)
    handle_w = 110 * scale
    handle_h = 100 * scale
    handle_x = (W - handle_w) // 2
    handle_y = int(bag_y - 48 * scale)
    
    # Draw Handle shadow
    draw.arc([handle_x, handle_y + 4*scale, handle_x + handle_w, handle_y + handle_h + 4*scale], start=180, end=0, fill=(0, 40, 20, 100), width=int(16*scale))
    # Draw Handle gold
    draw.arc([handle_x, handle_y, handle_x + handle_w, handle_y + handle_h], start=180, end=0, fill=c_gold, width=int(16*scale))
    draw.arc([handle_x + 2*scale, handle_y + 2*scale, handle_x + handle_w - 2*scale, handle_y + handle_h - 2*scale], start=180, end=0, fill=c_gold_light, width=int(6*scale))
    
    # Handle metal rivets
    rivet_r = 10 * scale
    draw.ellipse([handle_x - 3*scale, handle_y + handle_h//2 - 2*scale, handle_x + rivet_r*2 - 3*scale, handle_y + handle_h//2 + rivet_r*2 - 2*scale], fill=c_gold_light, outline=(180, 100, 0), width=int(2*scale))
    draw.ellipse([handle_x + handle_w - rivet_r*2 + 3*scale, handle_y + handle_h//2 - 2*scale, handle_x + handle_w + 3*scale, handle_y + handle_h//2 + rivet_r*2 - 2*scale], fill=c_gold_light, outline=(180, 100, 0), width=int(2*scale))
    
    # Bag Body (Pure clean White with Gold trimming and subtle depth)
    bag_radius = 36 * scale
    # Bag drop shadow
    draw.rounded_rectangle([bag_x, bag_y + 6*scale, bag_x + bag_w, bag_y + bag_h + 6*scale], radius=bag_radius, fill=(0, 30, 20, 90))
    # Bag solid white body
    draw.rounded_rectangle([bag_x, bag_y, bag_x + bag_w, bag_y + bag_h], radius=bag_radius, fill=(255, 255, 255, 255), outline=c_gold, width=int(6*scale))
    
    # Subtle top fold / bag cuff
    draw.line([(bag_x + 18*scale, bag_y + 36*scale), (bag_x + bag_w - 18*scale, bag_y + 36*scale)], fill=(240, 240, 240), width=int(3*scale))
    
    # 3. Inside Bag: Stylized Urdu 'ت' + Reseller Growth
    # Center of bag:
    cx = W // 2
    cy = bag_y + bag_h // 2 + 10 * scale
    
    # Swoosh base of 'ت' (Smiling confident curve)
    curve_w = 140 * scale
    curve_h = 75 * scale
    curve_box = [cx - curve_w//2, cy - 10*scale, cx + curve_w//2, cy + curve_h]
    draw.arc(curve_box, start=15, end=165, fill=(4, 120, 87), width=int(17*scale))
    
    # Left and Right upturned terminals of 'ت'
    left_x = cx - curve_w//2 + 5*scale
    left_y = cy + 20*scale
    draw.line([(left_x, left_y), (left_x + 12*scale, left_y - 28*scale)], fill=(4, 120, 87), width=int(16*scale))
    
    right_x = cx + curve_w//2 - 5*scale
    right_y = cy + 20*scale
    draw.line([(right_x, right_y), (right_x - 12*scale, right_y - 28*scale)], fill=(4, 120, 87), width=int(16*scale))
    
    # Twin Dots of 'ت' (Distinctive gold diamond / stars)
    dot_size = 14 * scale
    dot_y = cy - 25 * scale
    
    def draw_diamond(center_x, center_y, d_size, fill_color, border_color):
        pts = [
            (center_x, center_y - d_size),
            (center_x + d_size, center_y),
            (center_x, center_y + d_size),
            (center_x - d_size, center_y)
        ]
        draw.polygon(pts, fill=fill_color, outline=border_color)
        
    draw_diamond(cx - 20*scale, dot_y, dot_size, c_gold, (217, 119, 6))
    draw_diamond(cx + 20*scale, dot_y, dot_size, c_gold, (217, 119, 6))
    
    # 4. Text Branding below bag: "TEJARAT"
    # Draw stylized bold TEJARAT letters or clean wordmark
    try:
        # Try finding a bold sans font on Windows
        font_path = "C:/Windows/Fonts/arialbd.ttf"
        if not os.path.exists(font_path):
            font_path = "C:/Windows/Fonts/segoeuib.ttf"
        font_large = ImageFont.truetype(font_path, int(42 * scale))
        font_small = ImageFont.truetype(font_path, int(15 * scale))
    except Exception:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # Text "TEJARAT"
    title = "TEJARAT"
    bbox = draw.textbbox((0, 0), title, font=font_large)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (W - tw) // 2
    ty = int(395 * scale)
    
    # Drop shadow on text
    draw.text((tx, ty + 2*scale), title, font=font_large, fill=(0, 40, 20, 180))
    draw.text((tx, ty), title, font=font_large, fill=(255, 255, 255, 255))
    
    # Gold Subtitle: "PAKISTAN'S #1 RESELLER APP"
    subtitle = "RESELLER PLATFORM"
    s_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
    sw = s_bbox[2] - s_bbox[0]
    sx = (W - sw) // 2
    sy = int(ty + th + 14 * scale)
    
    # Pill badge behind subtitle
    pad_x = 16 * scale
    pad_y = 4 * scale
    draw.rounded_rectangle([sx - pad_x, sy - pad_y, sx + sw + pad_x, sy + s_bbox[3] - s_bbox[1] + pad_y], radius=8*scale, fill=(245, 158, 11, 230))
    draw.text((sx, sy), subtitle, font=font_small, fill=(20, 40, 30, 255))
    
    # Resize down with high-quality Lanczos resampling
    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    return final_img

# Generate all required icon files
os.makedirs("markaz_assets", exist_ok=True)
logo_512 = create_tejarat_logo(512)
logo_512.save("markaz_assets/tejarat_logo.png")
logo_512.save("tejarat_logo.png")
print("Saved markaz_assets/tejarat_logo.png (512x512)")

# Generate launcher icons
launcher_targets = [
    ("android_source/res/drawable/ic_launcher.png", 192),
    ("android_source/res/mipmap-mdpi/ic_launcher.png", 48),
    ("android_source/res/mipmap-hdpi/ic_launcher.png", 72),
    ("android_source/res/mipmap-xhdpi/ic_launcher.png", 96),
    ("android_source/res/mipmap-xxhdpi/ic_launcher.png", 144),
    ("android_source/res/mipmap-xxxhdpi/ic_launcher.png", 192),
]

for path, sz in launcher_targets:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    icon = logo_512.resize((sz, sz), Image.Resampling.LANCZOS)
    icon.save(path)
    print(f"Saved {path} ({sz}x{sz})")

print("All logo and launcher icon assets created successfully!")
