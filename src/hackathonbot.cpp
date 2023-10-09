//
// Created by Ethan on 9/13/2023.
//

#include "hackathonbot.h"

HackathonBot::HackathonBot() {};

void HackathonBot::takeAction(float price) {
    if (!this->priceHistory.empty()) {
        if (price > this->priceHistory.back()) {
            this->priceUpDays++;
            this->priceDownDays = 0;
        }
        else if (price < this->priceHistory.back()) {
            this->priceDownDays++;
            this->priceUpDays = 0;
        }
    }
    this->priceHistory.push_back(price);

    if (this->holding) { //sell case
        if (priceUpDays >= 52 || priceDownDays >= 47) {
            this->sell();
            return;
        }
        const float priceBought = this->priceHistory[0];
        if (price / priceBought > 1.89 || price / priceBought < 0.38) {
            this->sell();
            return;
        }

        //series window
        if (this->priceHistory.size() > 3) {
            const int n = this->priceHistory.size();
            //variable named num1num2 implies a ratio of the num1th last price / num2th last price
            const float thirdFourth = this->priceHistory[n - 3] / this->priceHistory[n - 4];
            const float secondThird = this->priceHistory[n - 2] / this->priceHistory[n - 3];
            const float firstSecond = this->priceHistory[n - 1] / this->priceHistory[n - 2];
            const float firstFourth = this->priceHistory[n - 1] / this->priceHistory[n - 4];

            if (thirdFourth >= 1.2 && secondThird <= 0.85 && firstSecond >= 1.3 && firstFourth >= 1.5) {
                this->sell();
                return;
            }
            if (thirdFourth <= 0.85 && secondThird >= 1.15 && firstSecond <= 0.75 && firstFourth <= 0.55) {
                this->sell();
                return;
            }

            if (this->priceHistory.size() >= 10) {
                float priceBought = this->priceHistory[0];
                for (const float& p : this->priceHistory) {
                    float priceRatio = p / priceBought;
                    if (std::abs(priceRatio - 1) > 0.05) {
                        return;
                    }
                }
                this->sell();
            }
        }

    }
    else {
        if (this->priceDownDays >= 5 || price < 52) {
            this->buy();
        }
    }

}

double HackathonBot::getBalance() {
    return this->balance;
}

bool HackathonBot::isHolding() {
    return this->holding;
}

void HackathonBot::buy() {
    this->holding = true;
}

void HackathonBot::sell() {
    this->holding = false;
    this->priceHistory.clear();
}