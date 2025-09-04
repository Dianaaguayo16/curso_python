try:
    import pygame
    import sys
    import os
    
    # Set environment variable to help with display issues
    os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
    
    # Initialize pygame
    pygame.init()
    
    # Check if display is available
    if pygame.display.get_init():
        print("✅ Pygame display initialized successfully!")
    else:
        print("❌ Pygame display failed to initialize")
        sys.exit(1)
    
    # Create the window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blue Sky - Press ESC or X to close")
    
    # RGB for sky blue
    sky_blue = (135, 206, 235)
    
    # Clock for controlling frame rate
    clock = pygame.time.Clock()
    
    print("🌤️  Blue Sky program started!")
    print("📱 Look for a blue window (might be behind other windows)")
    print("⌨️  Press ESC key or close the window to exit")
    print("🔄 Program is running...")
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Fill screen with sky blue
        screen.fill(sky_blue)
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(60)
    
    print("👋 Closing Blue Sky program...")
    pygame.quit()
    print("✅ Program closed successfully!")
    
except ImportError:
    print("❌ Pygame is not installed!")
    print("\n🔧 To fix this, install pygame:")
    print("1. Open Command Prompt or PowerShell as Administrator")
    print("2. Run: pip install pygame")
    print("3. Wait for installation to complete")
    print("4. Try running this program again")
    print("\n💡 Alternative commands:")
    print("   pip3 install pygame")
    print("   python -m pip install pygame")
    
except pygame.error as e:
    print(f"❌ Pygame error: {e}")
    print("\n🔧 Common solutions:")
    print("1. Restart your computer")
    print("2. Update your graphics drivers")
    print("3. Try running as Administrator")
    print("4. Check if another program is using the display")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    print("This might be a system configuration issue.")
    print("Try restarting your computer or running as Administrator.")