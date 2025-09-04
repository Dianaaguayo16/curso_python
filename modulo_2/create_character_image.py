# Create a simple character image
try:
    from PIL import Image, ImageDraw
    
    # Create a new image with white background
    img = Image.new('RGB', (50, 80), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw character body (orange rectangle)
    draw.rectangle([10, 30, 40, 70], fill='orange')
    
    # Draw character head (skin colored circle)
    draw.ellipse([15, 5, 35, 35], fill='#FFDAB9')  # Skin color
    
    # Draw eyes (black circles)
    draw.ellipse([22, 15, 28, 21], fill='black')  # Left eye
    draw.ellipse([32, 15, 38, 21], fill='black')  # Right eye
    
    # Draw arms
    draw.rectangle([0, 35, 10, 45], fill='orange')   # Left arm
    draw.rectangle([40, 35, 50, 45], fill='orange')  # Right arm
    
    # Draw legs (brown)
    draw.rectangle([15, 70, 25, 80], fill='brown')   # Left leg
    draw.rectangle([25, 70, 35, 80], fill='brown')   # Right leg
    
    # Save as BMP file
    img.save('character.bmp')
    print("✅ Character image 'character.bmp' created successfully!")
    print("📁 You can now use the original game_character.py program")
    
except ImportError:
    print("❌ PIL (Pillow) is not installed!")
    print("\n🔧 To install Pillow:")
    print("pip install Pillow")
    print("\n💡 Or use the fixed game_character.py program instead")
    
except Exception as e:
    print(f"❌ Error creating image: {e}")
    print("💡 Use the fixed game_character.py program instead")
