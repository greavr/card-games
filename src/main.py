#import pygame
import helpers.load_cards as card_helper

print(card_helper.Load_Conversation_Cards(file_path="./src/data/default_conversation.json"))




# pygame.init()

# #Create Canvas
# # CREATING CANVAS 
# canvas = pygame.display.set_mode((1500, 750)) 
  
# # TITLE OF CANVAS 
# pygame.display.set_caption("Hostage Negotiator - v0.1") 
# exit = False
  
# while not exit: 
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT: 
#             exit = True
#     pygame.display.update() 