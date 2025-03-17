import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ArrowBallComponent } from './arrow-ball/arrow-ball.component';

@NgModule({
  declarations: [
    AppComponent,
    ArrowBallComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
