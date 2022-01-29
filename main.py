def main():
  money = 550
  money_needed = [4, 7, 6]
  water = 400
  water_needed = [250, 350, 200]
  milk = 540
  milk_needed = [0, 75, 100]
  beans = 120
  beans_needed = [16, 20, 12]
  cups = 9

  while True:
      action = input('Write action (buy, fill, take, remaining, exit):')
      if action == 'remaining':
          print('The coffee machine has:')
          print(f'{water} of water')
          print(f'{milk} of milk')
          print(f'{beans} of coffee beans')
          print(f'{cups} of disposable cups')
          print(f'{money} of money')
      elif action == 'buy':
          ans = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
          if ans == 'back':
              continue
          coffee_type = int(ans)
          if water >= water_needed[coffee_type - 1]:
              if milk >= milk_needed[coffee_type - 1]:
                  if beans >= beans_needed[coffee_type - 1]:
                      water -= water_needed[coffee_type - 1]
                      milk -= milk_needed[coffee_type - 1]
                      beans -= beans_needed[coffee_type - 1]
                      cups -= 1
                      money += money_needed[coffee_type - 1]
                      print('I have enough resources, making you a coffee!')
                  else:
                      print('Sorry, not enough coffee beans!')
              else:
                  print('Sorry, not enough milk!')
          else:
              print('Sorry, not enough water!')
      elif action == 'fill':
          water += int(input('Write how many ml of water you want to add:'))
          milk += int(input('Write how many ml of milk you want to add:'))
          beans += int(input('Write how many grams of coffee beans you want to add:'))
          cups += int(input('Write how many disposable coffee cups you want to add:'))
      elif action == 'take':
          print(f'I gave you ${money}')
          money = 0
      elif action == 'exit':
          break
        

        
if __name__ == '__main__':
    main()
