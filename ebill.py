from lxml import etree
import random
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
cacns = config['InvoiceNameSpaces']['cacns']
cbcns = config['InvoiceNameSpaces']['cbcns']
NSMAP = {'cac': cacns, 'cbc': cbcns}
CBC = "{"+f"{NSMAP['cbc']}"+"}"
CAC = "{"+f"{NSMAP['cac']}"+"}"
payment_due_days = int(config['Supplier']['payment_due_days'])
currency = config['Supplier']['currency']
accounting_cost = config['Supplier']['accounting_cost']
buyer_reference = config['Supplier']['buyer_reference']
supplier_endpoint_id = config['Supplier']['supplier_endpoint_id']
supplier_party_id = config['Supplier']['supplier_party_id']
supplier_party_name = config['Supplier']['supplier_party_name']
supplier_street_name = config['Supplier']['supplier_street_name']
supplier_street_name2 = config['Supplier']['supplier_street_name2']
supplier_city_name = config['Supplier']['supplier_city_name']
supplier_postal_zone = config['Supplier']['supplier_postal_zone']
supplier_country = config['Supplier']['supplier_country']
supplier_tax_company_id = config['Supplier']['supplier_tax_company_id']
supplier_tax_scheme = config['Supplier']['supplier_tax_scheme']
supplier_registration_name = config['Supplier']['supplier_registration_name']
supplier_legal_entity_company_id = config['Supplier']['supplier_legal_entity_company_id']

customer_endpoint_id = config['Customer']['customer_endpoint_id']
customer_party_id = config['Customer']['customer_party_id']
customer_party_name = config['Customer']['customer_party_name']
customer_street_name = config['Customer']['customer_street_name']
customer_street_name2 = config['Customer']['customer_street_name2']
customer_city_name = config['Customer']['customer_city_name']
customer_postal_zone = config['Customer']['customer_postal_zone']
customer_country = config['Customer']['customer_country']
customer_tax_company_id = config['Customer']['customer_tax_company_id']
customer_tax_scheme = config['Customer']['customer_tax_scheme']
customer_registration_name = config['Customer']['customer_registration_name']
customer_legal_entity_company_id = config['Customer']['customer_legal_entity_company_id']
customer_contact_name = config['Customer']['customer_contact_name']
customer_telephone = config['Customer']['customer_telephone']
customer_electronic_mail = config['Customer']['customer_electronic_mail']

delivery_days = int(config['Delivery']['delivery_days'])
delivery_location_id = config['Delivery']['delivery_location_id']
delivery_street_name = config['Delivery']['delivery_street_name']
delivery_street_name2 = config['Delivery']['delivery_street_name2']
delivery_city_name = config['Delivery']['delivery_city_name']
delivery_postal_zone = config['Delivery']['delivery_postal_zone']
delivery_country = config['Delivery']['delivery_country']
delivery_party_name = config['Delivery']['delivery_party_name']

payment_means_code = config['Payment']['payment_means_code']
payee_financial_account_id = config['Payment']['payee_financial_account_id']
payee_account_name = config['Payment']['payee_account_name']
payee_financial_institute_id = config['Payment']['payee_financial_institute_id']
payment_terms_note = config['Payment']['payment_terms_note']

allowance_indicator = config['Allowance']['allowance_indicator']
allowance_reason = config['Allowance']['allowance_reason']
allowance_amount = config['Allowance']['allowance_amount']
allowance_tax_id = config['Allowance']['allowance_tax_id']
allowance_tax_percent = config['Allowance']['allowance_tax_percent']
allowance_tax_scheme_id = config['Allowance']['allowance_tax_scheme_id']

tax_amount = '0'
taxable_amount = '0'
tax_category_id = config['Tax']['tax_category_id']
tax_percent = config['Tax']['tax_percent']
tax_scheme_id = config['Tax']['tax_scheme_id']

line_extension_amount = '0'
tax_exclusive_amount = '0'
tax_inclusive_amount = '0'
charge_total_amount = allowance_amount
payable_amount = '0'
ELEMENT_DATA = {f'{CBC}'+'CustomizationID': 'urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0',
                f'{CBC}'+'ProfileID': 'urn:fdc:peppol.eu:2017:poacc:billing:01:1.0',
                f'{CBC}'+'ID': '1'+str(random.randint(10000000000, 99999999999)),
                f'{CBC}'+'IssueDate': str(datetime.date.today()),
                f'{CBC}'+'DueDate': str(datetime.date.today()+datetime.timedelta(days=payment_due_days)),
                f'{CBC}'+'InvoiceTypeCode': '380',
                f'{CBC}'+'DocumentCurrencyCode': currency,
                f'{CBC}'+'AccountingCost': accounting_cost,
                f'{CBC}'+'BuyerReference': buyer_reference,
                f'{CAC}'+'AccountingSupplierParty': {f'{CAC}'+'Party': {f'{CBC}'+'EndpointID': supplier_endpoint_id, f'{CAC}'+'PartyIdentification': {f'{CBC}'+'ID': supplier_party_id}, f'{CAC}'+'PartyName': {f'{CBC}'+'Name': supplier_party_name}, f'{CAC}'+'PostalAddress': {f'{CBC}'+'StreetName': supplier_street_name, f'{CBC}'+'AdditionalStreetName': supplier_street_name2, f'{CBC}'+'CityName': supplier_city_name, f'{CBC}'+'PostalZone': supplier_postal_zone, f'{CAC}'+'Country': {f'{CBC}'+'IdentificationCode': supplier_country}}, f'{CAC}'+'PartyTaxScheme': {f'{CBC}'+'CompanyID': supplier_tax_company_id, f'{CAC}'+'TaxScheme': {f'{CBC}'+'ID': supplier_tax_scheme}}, f'{CAC}'+'PartyLegalEntity': {f'{CBC}'+'RegistrationName': supplier_registration_name, f'{CBC}'+'CompanyID': supplier_legal_entity_company_id}}},
                f'{CAC}'+'AccountingCustomerParty': {f'{CAC}'+'Party': {f'{CBC}'+'EndpointID': customer_endpoint_id, f'{CAC}'+'PartyIdentification': {f'{CBC}'+'ID': customer_party_id}, f'{CAC}'+'PartyName': {f'{CBC}'+'Name': customer_party_name}, f'{CAC}'+'PostalAddress': {f'{CBC}'+'StreetName': customer_street_name, f'{CBC}'+'AdditionalStreetName': customer_street_name2, f'{CBC}'+'CityName': customer_city_name, f'{CBC}'+'PostalZone': customer_postal_zone, f'{CAC}'+'Country': {f'{CBC}'+'IdentificationCode': customer_country}}, f'{CAC}'+'PartyTaxScheme': {f'{CBC}'+'CompanyID': customer_tax_company_id, f'{CAC}'+'TaxScheme': {f'{CBC}'+'ID': customer_tax_scheme}}, f'{CAC}'+'PartyLegalEntity': {f'{CBC}'+'RegistrationName': customer_registration_name, f'{CBC}'+'CompanyID': customer_legal_entity_company_id}, f'{CAC}'+'Contact': {f'{CBC}'+'Name': customer_contact_name, f'{CBC}'+'Telephone': customer_telephone, f'{CBC}'+'ElectronicMail': customer_electronic_mail}}},
                f'{CAC}'+'Delivery': {f'{CBC}'+'ActualDeliveryDate': str(datetime.date.today()+datetime.timedelta(days=delivery_days)), f'{CAC}'+'DeliveryLocation': {f'{CBC}'+'ID': delivery_location_id, f'{CAC}'+'Address': {f'{CBC}'+'StreetName': delivery_street_name, f'{CBC}'+'AdditionalStreetName': delivery_street_name2, f'{CBC}'+'CityName': delivery_city_name, f'{CBC}'+'PostalZone': delivery_postal_zone, f'{CAC}'+'Country': {f'{CBC}'+'IdentificationCode': delivery_country}}}, f'{CAC}'+'DeliveryParty': {f'{CAC}'+'PartyName': {f'{CBC}'+'Name': delivery_party_name}}},
                f'{CAC}'+'PaymentMeans': {f'{CBC}'+'PaymentMeansCode': payment_means_code, f'{CBC}'+'PaymentID': 'P-'+str(random.randint(10000000000, 99999999999)), f'{CAC}'+'PayeeFinancialAccount': {f'{CBC}'+'ID': payee_financial_account_id, f'{CBC}'+'Name': payee_account_name, f'{CAC}'+'FinancialInstitutionBranch': {f'{CBC}'+'ID': payee_financial_institute_id}}},
                f'{CAC}'+'PaymentTerms': {f'{CBC}'+'Note': payment_terms_note},
                f'{CAC}'+'AllowanceCharge': {f'{CBC}'+'ChargeIndicator': allowance_indicator, f'{CBC}'+'AllowanceChargeReason': allowance_reason, f'{CBC}'+'Amount': allowance_amount, f'{CAC}'+'TaxCategory': {f'{CBC}'+'ID': allowance_tax_id, f'{CBC}'+'Percent': allowance_tax_percent, f'{CAC}'+'TaxScheme': {f'{CBC}'+'ID': allowance_tax_scheme_id}}},
                f'{CAC}'+'TaxTotal': {f'{CBC}'+'TaxAmount': tax_amount, f'{CAC}'+'TaxSubtotal': {f'{CBC}'+'TaxableAmount': taxable_amount, f'{CBC}'+'TaxAmount': tax_amount, f'{CAC}'+'TaxCategory': {f'{CBC}'+'ID': tax_category_id, f'{CBC}'+'Percent': tax_percent, f'{CAC}'+'TaxScheme': {f'{CBC}'+'ID': tax_scheme_id}}}},
                f'{CAC}'+'LegalMonetaryTotal': {f'{CBC}'+'LineExtensionAmount': line_extension_amount, f'{CBC}'+'TaxExclusiveAmount': tax_exclusive_amount, f'{CBC}'+'TaxInclusiveAmount': tax_inclusive_amount, f'{CBC}'+'ChargeTotalAmount': charge_total_amount, f'{CBC}'+'PayableAmount': payable_amount},

                }

invoice_line_id = 0
invoice_tax_class = tax_category_id
invoice_tax_percent = tax_percent
invoice_tax_scheme = tax_scheme_id

root = etree.Element('Invoice', xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2", nsmap=NSMAP)
xml = etree.ElementTree(root)

for element in ELEMENT_DATA:
    elem = etree.SubElement(root, element)
    if isinstance(ELEMENT_DATA[element], dict):
        for key in ELEMENT_DATA[element]:
            key_elem = etree.SubElement(elem, key)
            if isinstance(ELEMENT_DATA[element][key], dict):
                for key_elem_key in ELEMENT_DATA[element][key]:
                    key_elem_key_child = etree.SubElement(key_elem, key_elem_key)
                    if isinstance(ELEMENT_DATA[element][key][key_elem_key], dict):
                        for key_elem_key_elem in ELEMENT_DATA[element][key][key_elem_key]:
                            key_elem_key_child_elem = etree.SubElement(key_elem_key_child, key_elem_key_elem)
                            if isinstance(ELEMENT_DATA[element][key][key_elem_key][key_elem_key_elem], dict):
                                for key_elem_key_elem_key in ELEMENT_DATA[element][key][key_elem_key][key_elem_key_elem]:
                                    key_elem_key_child_elem_child = etree.SubElement(key_elem_key_child_elem, key_elem_key_elem_key)
                                    key_elem_key_child_elem_child.text = ELEMENT_DATA[element][key][key_elem_key][key_elem_key_elem][key_elem_key_elem_key]
                            else:
                                key_elem_key_child_elem.text = ELEMENT_DATA[element][key][key_elem_key][key_elem_key_elem]
                    else:
                        key_elem_key_child.text = ELEMENT_DATA[element][key][key_elem_key]

            else:
                key_elem.text = ELEMENT_DATA[element][key]
    else:
        elem.text = ELEMENT_DATA[element]

ATTRIBS = {'/Invoice/cac:AccountingSupplierParty/cac:Party/cbc:EndpointID': {'schemeID': '0088'}, '/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:EndpointID': {'schemeID': '0002'}, '/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID': {'schemeID': '0002'}, '/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID': {'schemeID': '0183'}, '/Invoice/cac:Delivery/cac:DeliveryLocation/cbc:ID': {'schemeID': '0088'}, '/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode': {'name': 'Credit transfer'}, '/Invoice/cac:AllowanceCharge/cbc:Amount': {'currencyID': 'EUR'}, '/Invoice/cac:TaxTotal/cbc:TaxAmount': {'currencyID': 'EUR'}, '/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount': {'currencyID': 'EUR'}, '/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount': {'currencyID': 'EUR'}, '/Invoice/cac:LegalMonetaryTotal/*': {'currencyID': 'EUR'}}

for attrib in ATTRIBS:
    para = root.xpath(attrib, namespaces=NSMAP)
    for attrib_name in ATTRIBS[attrib]:
        for i in para:
            i.attrib[attrib_name] = ATTRIBS[attrib][attrib_name]

not_done = 'Y'

while not_done == 'Y' or not_done == 'y':
    root2 = etree.Element('Invoice', xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2", nsmap=NSMAP)
    invoice_line_id += 1
    invoice_line_text = input('Invoice line text?: ')  # invoice_line_text = 'Konteringsstreng'
    invoice_orderline_id = input('Invoice line order id?: ')  # invoice_orderline_id = '123'
    invoice_origin_country = input('Invoice country origin?: ')  # invoice_origin_country = 'NO'
    invoice_commodity_class = input('Commodity class number?: ')  # invoice_commodity_class = '09348023'
    invoice_item_name = input('Name of item?: ')
    invoice_item_id = input('ID-nr of item?: ')   # invoice_item_id = '21382183120983'
    invoice_item_description = input('Description of item?: ')
    invoiced_quantity = input('Invoiced quantity?: ')
    invoice_price = input('Price per unit?: ')
    invoice_line_ext_amount = float(invoiced_quantity) * float(invoice_price)
    line_extension_amount = float(line_extension_amount) + invoice_line_ext_amount
    tax_exclusive_amount = line_extension_amount + int(charge_total_amount)
    tax_amount = tax_exclusive_amount * float(tax_percent) / 100
    tax_inclusive_amount = tax_exclusive_amount + tax_amount
    payable_amount = tax_inclusive_amount
    INVOICE_LINE = {f'{CAC}' + 'InvoiceLine': {f'{CBC}' + 'ID': str(invoice_line_id),
                                               f'{CBC}' + 'InvoicedQuantity': invoiced_quantity,
                                               f'{CBC}' + 'LineExtensionAmount': str(invoice_line_ext_amount),
                                               f'{CBC}' + 'AccountingCost': invoice_line_text,
                                               f'{CAC}' + 'OrderLineReference': {
                                                   f'{CBC}' + 'LineID': invoice_orderline_id},
                                               f'{CAC}' + 'Item': {f'{CBC}' + 'Description': invoice_item_description,
                                                                   f'{CBC}' + 'Name': invoice_item_name,
                                                                   f'{CAC}' + 'StandardItemIdentification': {
                                                                       f'{CBC}' + 'ID': invoice_item_id},
                                                                   f'{CAC}' + 'OriginCountry': {
                                                                       f'{CBC}' + 'IdentificationCode': invoice_origin_country},
                                                                   f'{CAC}' + 'CommodityClassification': {
                                                                       f'{CBC}' + 'ItemClassificationCode': invoice_commodity_class},
                                                                   f'{CAC}' + 'ClassifiedTaxCategory': {
                                                                       f'{CBC}' + 'ID': invoice_tax_class,
                                                                       f'{CBC}' + 'Percent': invoice_tax_percent,
                                                                       f'{CAC}' + 'TaxScheme': {
                                                                           f'{CBC}' + 'ID': invoice_tax_scheme}}},
                                               f'{CAC}' + 'Price': {f'{CBC}' + 'PriceAmount': invoice_price}}

                    }

    for element in INVOICE_LINE:
        invoice_elem = etree.SubElement(root2, element)
        if isinstance(INVOICE_LINE[element], dict):
            for key in INVOICE_LINE[element]:
                key_elem = etree.SubElement(invoice_elem, key)
                if isinstance(INVOICE_LINE[element][key], dict):
                    for key_elem_key in INVOICE_LINE[element][key]:
                        key_elem_key_child = etree.SubElement(key_elem, key_elem_key)
                        if isinstance(INVOICE_LINE[element][key][key_elem_key], dict):
                            for key_elem_key_elem in INVOICE_LINE[element][key][key_elem_key]:
                                key_elem_key_child_elem = etree.SubElement(key_elem_key_child, key_elem_key_elem)
                                if isinstance(INVOICE_LINE[element][key][key_elem_key][key_elem_key_elem], dict):
                                    for key_elem_key_elem_key in INVOICE_LINE[element][key][key_elem_key][key_elem_key_elem]:
                                        key_elem_key_child_elem_child = etree.SubElement(key_elem_key_child_elem, key_elem_key_elem_key)
                                        key_elem_key_child_elem_child.text = INVOICE_LINE[element][key][key_elem_key][key_elem_key_elem][key_elem_key_elem_key]
                                else:
                                    key_elem_key_child_elem.text = INVOICE_LINE[element][key][key_elem_key][key_elem_key_elem]
                        else:
                            key_elem_key_child.text = INVOICE_LINE[element][key][key_elem_key]

                else:
                    key_elem.text = INVOICE_LINE[element][key]
        else:
            invoice_elem.text = INVOICE_LINE[element]

    LEGAL_MONETARY_TOTAL = {'/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount': f'{line_extension_amount}', '/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount': f'{tax_exclusive_amount}', '/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount': f'{tax_inclusive_amount}', '/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount': f'{charge_total_amount}', '/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount': f'{payable_amount}'}

    for path in LEGAL_MONETARY_TOTAL:
        destination = root.xpath(path, namespaces=NSMAP)
        for i in destination:
            i.text = LEGAL_MONETARY_TOTAL[path]

    TAX_TOTAL = {'/Invoice/cac:TaxTotal/cbc:TaxAmount': f'{tax_amount}',
                            '/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount': f'{tax_exclusive_amount}',
                            '/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount': f'{tax_amount}'}

    for path in TAX_TOTAL:
        destination = root.xpath(path, namespaces=NSMAP)
        for i in destination:
            i.text = TAX_TOTAL[path]

    INVOICE_LINE_ATTRIBS = {'/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity': {'unitCode': 'DAY'}, '/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount': {'currencyID': 'EUR'}, '/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID': {'schemeID': '0088'}, '/Invoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:ItemClassificationCode': {'listID': 'SRV'}, '/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount': {'currencyID': 'EUR'}}

    for path in INVOICE_LINE_ATTRIBS:
        attribute = root2.xpath(path, namespaces=NSMAP)
        for attrib_name in INVOICE_LINE_ATTRIBS[path]:
            for i in attribute:
                i.attrib[attrib_name] = INVOICE_LINE_ATTRIBS[path][attrib_name]

    root.insert(len(root), root2.getchildren()[0])

    not_done = input('Do you want to add another Invoice line?(Y/y): ')



xml.write('ubl_invoice.xml', encoding='utf-8',
          xml_declaration=True,
          pretty_print=True)

