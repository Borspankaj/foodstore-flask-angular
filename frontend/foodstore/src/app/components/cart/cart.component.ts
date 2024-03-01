import { Component } from '@angular/core';
import { CartService } from 'src/app/services/cart.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent {

  cart: any;
  constructor(
    private cartService: CartService ,
    private router : Router) {}

  ngOnInit() {
    this.fetchCartItems();
  }
  

  fetchCartItems() {
    this.cartService.getCartItems().subscribe(
      (data) => {
        this.cart = data;
        console.log(this.cart)
      },
      (error) => {
        console.error('Error fetching cart items:', error);
      }
    );
  }

  deleteCartItem(bookId: any) {
    this.cartService.deleteCartItem(bookId).subscribe(
      () => {
        console.log('Item deleted from cart:', bookId);
        this.fetchCartItems();
      },
      (error) => {
        console.error('Error deleting item from cart:', error);
      }
    );
  }


  placeOrder() {
    this.cartService.placeOrder().subscribe(
      () => {
        this.router.navigate(['/homepage'])
      },
      (error) => {
        console.error('Error deleting item from cart:', error);
      }
    );
  }

}
