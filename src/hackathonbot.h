//
// Created by Ethan on 9/13/2023.
//

#include <vector>
#include <cstdlib>
#include "action.h"

#ifndef LEARNSOMETHING_HACKATHONBOT_H
#define LEARNSOMETHING_HACKATHONBOT_H

class HackathonBot {
    public:
    HackathonBot();
    void takeAction(float price);
    double getBalance();
    bool isHolding();
    private:
    double balance = 0;
    bool holding = false;
    int priceDownDays = 0;
    int priceUpDays = 0;
    std::vector<float> priceHistory;
    void buy();
    void sell();
};

#endif //LEARNSOMETHING_HACKATHONBOT_H
