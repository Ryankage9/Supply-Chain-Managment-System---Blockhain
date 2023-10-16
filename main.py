from user import check_user_type, register_user, login_user  
from transaction import add_new_product, start_delivery, confirm_receipt, raise_dispute, view_completed_deliveries, view_pending_deliveries
from block import Block, blockchain

    
#Main Function
if __name__ == "__main__":
    while True:
        print("\n")
        print("1. Register New User")
        print("2. Add New Product")
        print("3. Start Delivery")
        print("4. Confirm Receipt")
        print("5. Raise a Dispute")
        print("6. View Blockchain")
        print("7. View Completed Deliveries")
        print("8. View Pending Deliveries")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_type = input("Enter user type (Manufacturer/Distributor/Client): ")
            if not check_user_type(user_type):
                continue
            register_user(user_type)
        
        elif choice == '2':
            user_type = input("Enter your user type: ")
            if not check_user_type(user_type):
                continue
            username = login_user(user_type)
            add_new_product(username, user_type)
        
        elif choice == '3':
            user_type = input("Enter your user type: ")
            if not check_user_type(user_type):
                continue
            username = login_user(user_type)
            start_delivery(username, user_type)    
        
        elif choice == '4':
            user_type = input("Enter your user type: ")
            if not check_user_type(user_type):
                continue
            username = login_user(user_type)
            confirm_receipt(username, user_type)
        
        elif choice == '5':
            user_type = input("Enter your user type: ")
            if not check_user_type(user_type):
                continue
            username = login_user(user_type)
            raise_dispute(username, user_type)    
        
        elif choice == '6':
            user_type = input("Enter your user type: ")
            if not check_user_type(user_type):
                continue
            username = login_user(user_type)
            if not blockchain:
                print("Blockchain currently empty")
            else:
                Block.view_blockchain(username)
        
        elif choice == '7':
            user_type = input("Enter your user type: ")
            if not check_user_type(user_type):
                continue
            username = login_user(user_type)
            view_completed_deliveries(username)        
        
        elif choice == '8':
            user_type = input("Enter your user type: ")
            if not check_user_type(user_type):
                continue
            username = login_user(user_type)
            view_pending_deliveries(username)
        
        elif choice == '9':
            print("Exiting Program...")
            break
        else:
            print("Invalid choice. Please try again.")