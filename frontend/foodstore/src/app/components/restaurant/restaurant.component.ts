import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RestaurantService } from 'src/app/services/restaurant.service';
import { Router } from '@angular/router';
import { MenuService } from 'src/app/services/menu.service';
import { CartService } from 'src/app/services/cart.service';
import { AccountService } from 'src/app/services/account.service';
import { OrderService } from 'src/app/services/order.service';
@Component({
  selector: 'app-restaurant',
  templateUrl: './restaurant.component.html',
  styleUrls: ['./restaurant.component.css']
})
export class RestaurantComponent {
  restaurantId : any
  restaurantData : any
  restaurantMenu : any
  orders : any
  quantity = 0
  constructor(
    private route : ActivatedRoute ,
    private restaurantService : RestaurantService ,
    private router : Router ,
    private menuService : MenuService ,
    private cartService : CartService ,
    private accountService : AccountService ,
    private orderService : OrderService

  ) {
    this.restaurantId = this.route.snapshot.paramMap.get('id');
  }

  ngOnInit() {
    this.fetchRestaurantInfo();
    this.fetchRestaurantMenu() ;
    this.fetchOwnerOrders()
  }

  fetchRestaurantInfo() {
    this.restaurantService.getRestaurantById(this.restaurantId).subscribe(
      (data) => {
        this.restaurantData = data;
        console.log('Restaurant data:', this.restaurantData);
      },
      (error) => {
        console.error('Error fetching restaurant data:', error);
       
      }
    );
  }

  fetchRestaurantMenu() {
    this.restaurantService.getRestaurantMenu(this.restaurantId).subscribe(
      (menu) => {
        this.restaurantMenu = menu;
        console.log('Restaurant menu:', this.restaurantMenu);
      },
      (error) => {
        console.error('Error fetching restaurant menu:', error);
        
      }
    );
  }

  addMenu() {
    this.router.navigate(['/add-menu', this.restaurantId]);
  }

  editMenu(menuId : any) {
    console.log(menuId)
    this.router.navigate(['/edit-menu' , menuId]) ;
  }

  deleteMenu(menuId : any) {
    this.menuService.deleteMenu(menuId).subscribe(
      (response) => {
        this.router.navigate(['/owner-home'])
      },
      (error) => {
        console.error('Error fetching restaurant menu:', error);
        
      }
    );

  }

  addToCart(menuId: any , restaurantId : any , quantity : number) {
    this.cartService.addToCart(menuId , quantity , restaurantId).subscribe(
      (response) => {
        alert("added")
        
      },
      (error) => {
        console.error('Error fetching restaurant menu:', error);
        
      }
    );

  }

  decrementQuantity() {
    this.quantity = this.quantity - 1

    }

  incrementQuantity(){
    this.quantity = this.quantity + 1
  }

  getRole() {
    
    return this.accountService.getRole()

  }

  fetchOwnerOrders(){
    this.orderService.getOrdersByRestaurant(this.restaurantId).subscribe(
      (data) => {
        this.orders = data.data.data;
        console.log('Restaurant menu:', this.orders);
      },
      (error) => {
        console.error('Error fetching restaurant menu:', error);
        
      }
    );

  }
  updateOrderStatus(order: any) {
    
    console.log('Updating order status:', order.newStatus);
    this.orderService.updateStatus(order.order_id , order.newStatus).subscribe(
      (data) => {
        this.router.navigate(['/restaurant', this.restaurantId]);
      },
      (error) => {
        console.error('Error fetching restaurant menu:', error);
        
      }
    );
    
  }
}
