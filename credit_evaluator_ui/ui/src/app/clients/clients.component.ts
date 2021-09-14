import { Component, OnInit } from '@angular/core';

import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-clients',
  templateUrl: './clients.component.html',
  styleUrls: ['./clients.component.css'],
})
export class ClientsComponent implements OnInit {
  constructor(private http: HttpClient) {}

  clients: any = [];

  ngOnInit(): void {
    this.refreshList();
  }

  refreshList() {
    this.http
      .get<any>(environment.API_URL + 'credits/clients')
      .subscribe((data) => {
        this.clients = data;
      });
  }
}
