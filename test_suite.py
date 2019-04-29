from unittest import TestLoader,TestSuite,TextTestRunner
from tests.AudienceBuilder.test_1_verify_audience_explorer import audience_explorer
from tests.AudienceBuilder.test_2_verify_audience_distribute import audience_distribution
from tests.AudienceBuilder.test_3_verify_audience_rename import audience_rename
from tests.AudienceBuilder.test_4_verify_audience_compare import audience_compare
from tests.AudienceBuilder.test_5_verify_copy_audience_criteria import audience_copy_criteria
from tests.AudienceBuilder.test_6_verify_audience_criteria_parenthesis import audience_criteria_parenthesis
from tests.AudienceBuilder.test_7_verify_rate_card import cpm_rate
from tests.AudienceBuilder.test_8_verify_audience_history import audience_history
# import HtmlTestRunner


# get all tests from class
audience_explorer               = TestLoader().loadTestsFromTestCase(audience_explorer)
audience_distribution           = TestLoader().loadTestsFromTestCase(audience_distribution)
audience_rename                 = TestLoader().loadTestsFromTestCase(audience_rename)
audience_compare                = TestLoader().loadTestsFromTestCase(audience_compare)
audience_copy_criteria          = TestLoader().loadTestsFromTestCase(audience_copy_criteria)
audience_criteria_parenthesis   = TestLoader().loadTestsFromTestCase(audience_criteria_parenthesis)
cpm_rate                        = TestLoader().loadTestsFromTestCase(cpm_rate)
audience_history                = TestLoader().loadTestsFromTestCase(audience_history)

# create a test suite
test_suite = TestSuite([
                        # audience_explorer,
                        audience_distribution
                        # audience_rename,
                        # audience_compare
                        # audience_copy_criteria,
                        # audience_criteria_parenthesis
                        # cpm_rate
                        # audience_history
                        ])
TextTestRunner(verbosity=2).run(test_suite)
# test_result = TextTestRunner(verbosity=2).run(test_suite)
# testRunner  = HtmlTestRunner.HTMLTestRunner(output='E:\BitBucket\AudienceBuilder')
# testRunner.run(test_suite)