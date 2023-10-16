1. Information
 Aryan Vatsa - 2020A3PS2124H
 Birla Institute of Technology and Science Pilani, Hydddd campus

3. Code Flow:
- The code starts by defining several data structures and classes, including a Block class to represent blocks in the blockchain.
- It maintains a blockchain to record transactions and product movements, a list of ongoing deliveries, and a list of completed transactions. There are also data structures to store user information, products, and delegates.
- The Block class is used to create new blocks in the blockchain. It calculates the Merkle root, computes the hash of the block, and incorporates a simple Delegated Proof of Stake (DPoS) consensus algorithm
- User management is implemented with the ability to register, log in, and verify user credentials. Users are categorized as Manufacturers, Distributors, and Clients.
- Manufacturers can add new products to the product list, which are then available for distribution.
- Distributors can initiate product deliveries to Clients, marking the shipment timestamp.
- Clients can confirm the receipt of delivered products, marking the receive timestamp. They can also raise disputes for incorrect deliveries.
- Completed transactions are added to the blockchain, and every three completed transactions trigger the mining of a new block.
- Users can view the blockchain, completed deliveries, and ongoing deliveries.
- The main program runs in an infinite loop, presenting a menu to the user to choose from various options.

3. Functionalities Provided:
- User Registration: Users can register as Manufacturers, Distributors, or Clients, providing their username, password, and ID. Distributors and Clients need to deposit a security amount.
- User Authentication: Users can log in with their username and password.
- Product Management: Manufacturers can add new products to the product list, which includes a unique product ID and production timestamp.
Distributors can initiate deliveries of products to Clients.
- Product Confirmation: Clients can confirm the receipt of products. Completed transactions are added to the blockchain.
- Dispute Resolution: Clients can raise disputes for incorrect deliveries, leading to the deduction of funds from either the client's security deposit or the distributor's security deposit.
- Blockchain Management: Users can view the blockchain, displaying block details, including transaction information.
- Transaction Mining: Mining is triggered every three completed transactions, creating a new block with Delegated Proof of Stake (DPoS) consensus algorithm.
- Delivery Tracking: Users can view ongoing deliveries and completed deliveries.
