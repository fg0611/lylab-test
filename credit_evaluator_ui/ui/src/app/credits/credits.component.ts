import { Component, OnInit } from '@angular/core';

import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-credits',
  templateUrl: './credits.component.html',
  styleUrls: ['./credits.component.css'],
})
export class CreditsComponent implements OnInit {
  constructor(private http: HttpClient) {}

  credits: any = [];

  ngOnInit(): void {
    this.refreshList();
  }

  refreshList() {
    this.http.get<any>(environment.API_URL + 'credits').subscribe((data) => {
      this.credits = data;
    });
  }

  approveClick(id: any) {
    if (confirm('Are you sure?')) {
      this.http
        .put(environment.API_URL + 'credits/' + id + '/approve', '')
        .subscribe((res) => {
          alert(JSON.stringify(res));
          this.refreshList();
        });
    }
  }

  denyClick(id: any) {
    if (confirm('Are you sure?')) {
      this.http
        .put(environment.API_URL + 'credits/' + id + '/deny', '')
        .subscribe((res) => {
          alert(JSON.stringify(res));
          this.refreshList();
        });
    }
  }
  deleteClick(id: any) {
    if (confirm('Are you sure?')) {
      this.http
        .delete(environment.API_URL + 'credits/' + id)
        .subscribe((res) => {
          alert(JSON.stringify(res));
          this.refreshList();
        });
    }
  }
}
