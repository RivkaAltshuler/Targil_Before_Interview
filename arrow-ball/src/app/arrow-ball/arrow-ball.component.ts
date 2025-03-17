import { Component } from '@angular/core';

@Component({
  selector: 'app-arrow-ball',
  templateUrl: './arrow-ball.component.html',
  styleUrls: ['./arrow-ball.component.css']
})
export class ArrowBallComponent {
  ballX = 0;
  ballY = 0;

  move(direction: string) {
    const step = 10; // קביעת מרחק התזוזה בכל לחיצה

    switch (direction) {
      case 'up':
        this.ballY -= step;
        break;
      case 'down':
        this.ballY += step;
        break;
      case 'left':
        this.ballX -= step;
        break;
      case 'right':
        this.ballX += step;
        break;
    }
  }
}