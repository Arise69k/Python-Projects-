#Mini Game Shop


coin = 500
inventory = []


while True:
	print("--------------MENU--------------------")
	print(" 1 View Shop")
	print(" 2 Buy item")
	print(" 3 View Inventory")
	print(" 4 View Coins")
	print(" 5 Exit")
	
	print("----------------------------------")
	
	choose = input("Choose: ").upper()
	
	
	#View Shop
	if choose == "1" or choose == "VIEW SHOP":
		print("-----------------SHOP-----------------")
		print(" 1 Sword               200 coins")
		print(" 2 Shield              150 coins")
		print(" 3 Health Potion        50 coins")
		print(" 4 Magic Wand          300 coins")
		print("----------------------------------")
		
	#Buy item
	elif choose == "2" or choose == "BUY ITEM":
		print("-----------------SHOP-----------------")
		print(" 1 Sword               200 coins")
		print(" 2 Shield              150 coins")
		print(" 3 Health Potion        50 coins")
		print(" 4 Magic Wand          300 coins")
		print("----------------------------------")
		
		shop = input("Buy : ").upper()
		
		#Sword
		if shop == "1" or shop == "SWORD":
			if coin >= 200:
				coin -= 200
				inventory.append("Sword")
				print("----------------------------------")
				print(" Sucessfully Purchased 'Sword' ")
				print("----------------------------------")	
			else:
				print("----------------------------------")
				print(" Insufficient Coins")
				print("----------------------------------")	
		#Shield
		elif  shop == "2" or shop == "SHIELD":
			if coin >= 150:
				coin -= 150
				inventory.append("Shield")
				print("----------------------------------")	
				print(" Sucessfully Purchased 'Shield' ")
				print("----------------------------------")
			else:
				print("----------------------------------")
				print(" Insufficient Coins")
				print("----------------------------------")
		
		#Health Potion
		elif shop == "3" or shop == "HEALTH POTION":
			if coin >= 50:
				coin -= 50
				inventory.append("Health Potion")
				print("----------------------------------")	
				print(" Sucessfully Purchased 'Health Potion' ")
				print("----------------------------------")
			else:
				print("----------------------------------")
				print(" Insufficient Coins")
				print("----------------------------------")
				
		#Magic Wand
		elif shop == "4" or shop == "MAGIC WAND":
				if coin >= 300:
					coin -= 300
					inventory.append("Magic Wand")
					print("----------------------------------")
					print(" Sucessfully Purchased 'Magic Wand' ")
					print("----------------------------------")
				else:
				    print("----------------------------------")
				    print(" Insufficient Coins")
				    print("----------------------------------")
		#Invalid
		else:
			print("----------------------------------")
			print(" Invalid Item Choice")
			print("----------------------------------")
				    
	
				
	#View Inventory
	elif choose == "3" or choose == "VIEW INVENTORY":
			 print("----------------------------------")
			 if inventory == []:
			 	print("Inventory Is Empty")
			 	print("----------------------------------")
			 	
			 
			 for i in inventory:
			 	print(i)			
			 
	#View Coins
	elif choose == "4" or choose == "VIEW COINS":
		print("----------------------------------")
		print(f"Coins {coin}")	
		print("----------------------------------")
		
	#Exit
	elif choose == "5" or choose == "EXIT":
		break
		
	#Invalid Choice
	else:
		print("----------------------------------")
		print(" Invalid Choice")
		print("----------------------------------")
	
		
				