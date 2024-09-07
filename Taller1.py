#Add Prodcut function
def addProduct(data):
     products[data[0]]=data[1];

#Delete product function
def removeProduct(key):
  products.pop(key);


#Update stock function
def updateStock(data):
   products[data[0]]=int(products.get(data[0]))+int(data[1]);

def showProducts():
  for key,value in products.items():
    print(f'Nombre:{key},Stock:{value}')
  print('\n\n')

#Verify low stock products function
def verifyStock():
  low_stock={}
  for i in products:
    temp=int(products.get(i))
    if temp<10:
          low_stock[i]=temp
  print(low_stock)
  orderLowStcok(low_stock) #order low stock  call function



# Order low stock products function
def orderLowStcok(data):
  stock_ordered = sorted(data.items(), key=lambda item: item[1])
  n=int(input('Cuantos productos con bajo stock desea ver?'))
  for i in range(n):
   print(f'{stock_ordered[i][0]}:{stock_ordered[i][1]}')



#Regsiter function
def register():
   registro=input('Formatos\n Para agregar o actualizar producto nombre:stock\nPara eliminar nombre\n').split(':');
   return registro;

"""
product{
  name:stock
}"""
products={
    'Manzana': 10,
    'Banana': 20,
    'Naranja': 15,
    'Uva': 5,
    'Pera': 8,
    'Sandía': 3,
    'Melón': 7,
    'Piña': 12,
    'Mango': 9,
    'Fresa': 25,
    'Cereza': 18,
    'Kiwi': 6,
    'Plátano': 11,
    'Limón': 22,
    'Pomelo': 4,
    'Granada': 16,
    'Higo': 14,
    'Ciruela': 19,
    'Papaya': 13,
    'Maracuyá': 17
}


#Main menu options
while True:
  new=input('1)Agregar productos \n2)Actualizar Stock \n3)Eliminar producto \n4)Verificar Stock \n5)Ver productos\n6)Salir\n\n ')
  if new=='1':
      while True :
            info = register();        #Register call function add format
            if info[0]!='salir':
               addProduct(info);      #Add call function
            else: break;
  elif new=='2':
      up_data=register();            #Register call funtion update format
      updateStock(up_data);          #Update call function
  elif new=='3':
      product_name=register();       #Register call function delete format
      removeProduct(product_name),   #Delete call function
  elif new=='4':
      verifyStock();                 #verify stock call function
  elif new=='5':
      showProducts();                #show products call function
  elif new=='6':
      break ;
  else:
    print('Opcion no valida \n\n');

