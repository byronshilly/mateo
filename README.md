# Project Mateo 
Project Mateo is an attempt to solve the problem of selling items online. 

The headaches associated with selling items on online marketplaces often circumvent people from selling their items at all. These headaches include:
- Taking pictures of your item that reflect its condition
- Creating a listing of your item with an informative description 
- Communicating with potential buyers 
- Packaging the item safely  
- Shipping the item 

The goal of project Mateo is to mitigate all these problems. The ideal scenario is: 
1. A listing for your item is created with one click of a button 
2. Communication between buyers/sellers does not happen
3. When an item is purchased, packaging is sent to the seller
4. The seller places the item inside the packaging and leaves it outside their door 
5. The package is picked up and shipped to the buyer

Achieving this ideal scenario poses a massive logistical problem since no two items are equal. However, this would be achievable and economically feasible with a particular item with the following characteristics: 
- All instances of the item are the same size
- All instances of the item are of the same condition
- All instances of this item do not need to be packaged with care (i.e. durability) 
- This item has a large "used" market (e.g. used cars) 

One such item is video games. Project Mateo plans to achieve the ideal scenario with an online marketplace for used video games:
1. A seller find their title on the platform and informs the system that they have a copy for sale, updating the system's internal inventory. 
2. When the copy is purchased by a buyer, Mateo will send a padded envelope to the seller with a shipping label directed to the buyer. 
3. The seller places their copy inside the envelope, attaches the shipping label, leaves it outside, and informs the system that their copy is ready for pickup. 
4. Mateo will utilize the USPS API to schedule a pickup for the package and send it to the buyer. 

### Project Components
Documentation for each component can be found in the respective component directories. 

- **Mateo:** Primary web service for the front-end application.
- **Website:** Front-end application.
- **Storekeeper:** CLI application for admin operations. 
