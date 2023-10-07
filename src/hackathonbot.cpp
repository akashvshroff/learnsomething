//
// Created by Ethan on 9/13/2023.
//

#include "hackathonbot.h"

HackathonBot::HackathonBot() {};

void HackathonBot::takeAction(float price) {
    return;
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
}