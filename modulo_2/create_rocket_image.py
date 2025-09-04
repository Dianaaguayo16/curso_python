# Create a simple rocket image
try:
    from PIL import Image, ImageDraw
    
    # Create a new image with transparent background
    img = Image.new('RGBA', (50, 80), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw rocket body (white rectangle)
    draw.rectangle([15, 20, 35, 70], fill='white')
    
    # Draw rocket tip (red triangle pointing up)
    tip_points = [(25, 0), (10, 25), (40, 25)]
    draw.polygon(tip_points, fill='red')
    
    # Draw rocket fins (red triangles at bottom)
    left_fin = [(0, 70), (15, 50), (20, 70)]
    right_fin = [(50, 70), (35, 50), (30, 70)]
    draw.polygon(left_fin, fill='red')
    draw.polygon(right_fin, fill='red')
    
    # Draw rocket window (blue circle)
    draw.ellipse([22, 35, 28, 41], fill='blue')
    
    # Draw rocket exhaust (orange rectangles at bottom)
    draw.rectangle([22, 70, 26, 78], fill='orange')
    draw.rectangle([24, 70, 28, 78], fill='orange')
    
    # Save as BMP file
    img.save('rocket.bmp')
    print("✅ Rocket image 'rocket.bmp' created successfully!")
    print("📁 You can now use the original rocket.py program")
    
except ImportError:
    print("❌ PIL (Pillow) is not installed!")
    print("\n🔧 To install Pillow:")
    print("pip install Pillow")
    print("\n💡 Or use the fixed rocket.py program instead")
    
except Exception as e:
    print(f"❌ Error creating image: {e}")
    print("💡 Use the fixed rocket.py program instead")
