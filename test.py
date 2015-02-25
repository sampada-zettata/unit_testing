import unittest
import simple_class2
import datetime 
import logging
import os,time,sys
# Import smtplib for the actual sending function
import smtplib, base64


# Import the email modules we'll need
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
from email import Encoders 

def main(out = sys.stderr, verbosity = 0):
	logging.basicConfig(filename='unit_test.log',format='%(asctime)s %(name)s %(levelname)-s %(message)s',level=logging.DEBUG)
	loader = unittest.TestLoader()
	suite = loader.loadTestsFromModule(sys.modules[__name__])		
	logging.info(unittest.TextTestRunner(out, verbosity = verbosity).run(suite))		
	

class SendStatusMail():
	sender = 'sampada@zettata.com'
	receivers = 'sampada@zettata.com'
	
	username = 'sampada@zettata.com'
	password = '1qazettata@B14'
	path = os.path.dirname(os.path.realpath('unit_test.log'))
	unittest_log_path = path+'/'+'unit_test.log'
	unittest_result_path = path+'/'+'testing_reports.out'
	files = [unittest_log_path, unittest_result_path];
	
	def sendMailWithAttachments(self):
		try:
			subject = "Unit-test-Reports-%s"%(time.strftime("%d/%m/%Y"))
			msg = MIMEMultipart('mixed')
			msg['Subject'] = subject
			msg['From'] = self.sender			
			msg['To'] = self.receivers			
			
			for f in self.files:
    				part = MIMEBase('application', "octet-stream")
    				part.set_payload(open(f, "rb").read())
    				Encoders.encode_base64(part)

    				attachment_name = f.split('/')[-1]
   				part.add_header('Content-Disposition', 'attachment; filename="'+attachment_name+'"')
    				msg.attach(part)
			
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			server.login(self.username,self.password)
			server.sendmail(self.sender, self.receivers, msg.as_string())
			server.quit()
		except Exception,e :
			logging.error('Unable to send mail', exc_info=True)
			raise e		

class SimpleTests(unittest.TestCase):
		
	obj = simple_class2.qury_testing()
	#obj.result_Value()
	flag = True

	def testBrand(self):
		try:								
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_1'),'Unit Test Fail for : Brand')		
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_1'),'Unit Test Fail for : Brand')
			self.assertEqual(True,self.obj.is_title_value('unit_test_1'),'Unit Test Fail for : Brand')
			logging.info("Successfully run test for Brand facet")					
		except Exception, e:
			logging.error("Unit Test Fail for : Brand ", exc_info=True)
			raise e
	
	def testCustomerRecommended(self):
		try: 				
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_2'),'Unit Test Fail for : CustomerRecommended')
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_2'),'Unit Test Fail for : CustomerRecommended')
			self.assertEqual(True,self.obj.is_title_value('unit_test_2'),'Unit Test Fail for : CustomerRecommended')
			logging.info("Successfully run test for CustomerRecommended facet")
		except Exception, e:
			logging.error("Unit Test Fail for : CustomerRecommended ", exc_info=True)
			raise e
					

	def testDeals(self):
		try:		
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_3'),'Unit Test Fail for : Deals') 
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_3'),'Unit Test Fail for : Deals')
			self.assertEqual(True,self.obj.is_title_value('unit_test_3'),'Unit Test Fail for : Deals') 
			logging.info("Successfully run test for Deals facet")	
		except Exception, e:
			logging.error("Unit Test Fail for : Deals", exc_info=True)
			raise e

	def testDepartment(self):
		try:		
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_4'),'Unit Test Fail for : Department')		
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_4'),'Unit Test Fail for : Department')
			self.assertEqual(True,self.obj.is_title_value('unit_test_4'),'Unit Test Fail for : Department')
			logging.info("Successfully run test for Department facet")		
		except Exception, e:
			logging.error("Unit Test Fail for : Department ", exc_info=True)
			raise e
		
	def testEnvironmental(self):
		try:		
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_5'),'Unit Test Fail for : Environmental') 
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_5'),'Unit Test Fail for : Environmental')
			self.assertEqual(True,self.obj.is_title_value('unit_test_5'),'Unit Test Fail for : Environmental')
			logging.info("Successfully run test for Environmental facet")
		except Exception, e:
			logging.error("Unit Test Fail for : Environmental ", exc_info=True)
			raise e
	
	def testInStoreAvailability(self):
		try:		
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_6'),'Unit Test Fail for : InStoreAvailability') 	
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_6'),'Unit Test Fail for : InStoreAvailability')
			self.assertEqual(True,self.obj.is_title_value('unit_test_6'),'Unit Test Fail for : InStoreAvailability')
			logging.info("Successfully run test for InStoreAvailability facet") 		
		except Exception, e:
			logging.error("Unit Test Fail for : InStoreAvailability", exc_info=True)
			raise e
		
	def testNewArrivals(self):
		try:					
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_7'),'Unit Test Fail for : NewArrivals')
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_7'),'Unit Test Fail for : NewArrivals')
			self.assertEqual(True,self.obj.is_title_value('unit_test_7'),'Unit Test Fail for : NewArrivals')
			logging.info("Successfully run test for NewArrivals facet")
		except Exception, e:
			logging.error("Text fail for Brand facet ", exc_info=True)
			raise e	
		
	def testRating(self):
		try:		 		
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_8'),'Unit Test Fail for : Rating') 
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_8'),'Unit Test Fail for : Rating') 
			logging.info("Successfully run test for Rating facet")
		except Exception, e:
			logging.error("Unit Test Fail for : Rating", exc_info=True)
			raise e
		
	def testBaseproduct(self):
		try:		
			#self.assertEqual(True,self.obj.is_Equal_value('unit_test_9'),'Unit Test Fail for : baseproduct')		
			self.assertTrue(self.obj.is_Num_Doc('unit_test_9'),'Unit Test Fail for : baseproduct')
			logging.info("Successfully run test for Baseproduct facet")		
		except Exception, e:
			logging.error("Unit Test Fail for : baseproduct ", exc_info=True)
			raise e
		
	def testInStock(self):	
		try:				
			#self.assertEqual(True,self.obj.is_Equal_value('unit_test_10'),'Unit Test Fail for : InStock')
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_10'),'Unit Test Fail for : InStock')			
			self.assertTrue(self.obj.is_In_Stock(),'Item in Out of Stock')
			logging.info("Successfully run test for InStock facet")
		except Exception, e:
			logging.error("Unit Test Fail for : InStock ", exc_info=True)
			raise e
		
if __name__ == '__main__':
	with open('testing_reports.out', 'a+') as f:	
		main(f)
	mail_service = SendStatusMail()
	mail_service.sendMailWithAttachments()
    #unittest.main()
