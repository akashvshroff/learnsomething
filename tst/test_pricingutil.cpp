#include <gtest/gtest.h>
#include <pricingutil.h>

TEST(sampleTest, sample) {
    EXPECT_EQ(4, 4);
}

TEST(testPricingUtil, calculateTheoreticalVal) {
    PricingUtil pricingUtil = PricingUtil();

    //standard case
    EXPECT_EQ(10, pricingUtil.calcVal(5, 1.1, 1));
    EXPECT_EQ(24, pricingUtil.calcVal(4, 2.1, 2));

    //edge case: 0 interest
    EXPECT_EQ(18, pricingUtil.calcVal(5, 0, 4));

    //edge case: -ve previous price
    EXPECT_EQ(-40, pricingUtil.calcVal(-5, 1.1, 4));

}