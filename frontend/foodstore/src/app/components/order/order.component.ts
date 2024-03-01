import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { OrderService } from 'src/app/services/order.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent {
  orders: any;

  constructor(private orderService: OrderService) {}

  ngOnInit() {
    this.fetchOrders();
  }

  fetchOrders()   {
    this.orderService.getOrders().subscribe(
      (data) => {
        console.log(data.data)
        this.orders = data.data;
      },
      (error) => {
        console.error('Error fetching orders:', error);
      }
    );
  }

}
