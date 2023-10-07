#include "pricingutil.h"

PricingUtil::PricingUtil() { this->val = 0; }

float PricingUtil::calcVal(float const prevPrice, float const interestRate, float const oleoConstant) {
    this->val = prevPrice * (0.9 + interestRate) * oleoConstant;
    return this->val;
}

float PricingUtil::getVal() { return this->val; }