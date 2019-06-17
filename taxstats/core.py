# to do: get all states for other dataset

import urllib

class taxstats(object):
    def __init__(self, table = 2, year: int = 2016, product = 'csv', level = None, state = None):
        self.table = str(table)
        self.maxyr = 2016
        self.mincompleteyr = 2012
        self.minstateyr = 1997
        self.mincountyyr = 2011
        self.year = year
        self.yy = int(str(year)[-2:])
        self.product = product
        self.level = level
        self.state = state
        if self.level == 'us':
            self.state = 'us'
        
        statenumbers = {
                    "al":1,
                    "ak":2,
                    "az":3,
                    "ar":4,
                    "ca":5,
                    "co":6,
                    "ct":7,
                    "de":8,
                    "dc":9,
                    "fl":10,
                    "ga":11,
                    "hi":12,
                    "id":13,
                    "il":14,
                    "in":15,
                    "ia":16,
                    "ks":17,
                    "ky":18,
                    "la":19,
                    "me":20,
                    "md":21,
                    "ma":22,
                    "mi":23,
                    "mn":24,
                    "ms":25,
                    "mo":26,
                    "mt":27,
                    "ne":28,
                    "nv":29,
                    "nh":30,
                    "nj":31,
                    "nm":32,
                    "ny":33,
                    "nc":34,
                    "nd":35,
                    "oh":36,
                    "ok":37,
                    "or":38,
                    "pa":39,
                    "ri":40,
                    "sc":41,
                    "sd":42,
                    "tn":43,
                    "tx":44,
                    "ut":45,
                    "vt":46,
                    "va":47,
                    "wa":48,
                    "wv":49,
                    "wi":50,
                    "wy":51,
                    "oa":52,
                    "us":53
                    }
        self.stnum = None
        try:
            self.stnum = statenumbers[self.state]
        except:
            pass
        
        #pseudo code for errors!
        if table == "2":
            if self.product not in ['csv', 'xls']:
                raise ValueError("Product must be 'csv' or 'xls'")
            if self.product == 'csv':
                if (self.level != None or self.state != None):
                    raise ValueError("If product is 'csv', level and state must be empty")
            elif self.product == 'xls':
                if self.level not in ['us', 'state', 'county', '*']:
                    raise ValueError("if product is 'xls', level must be 'us', 'state', 'county', or '*'")
                if self.level in ['us', '*'] and self.state != None:
                    raise ValueError("If level is '*' or 'us', state must be empty")
                if self.level in ['state', 'county'] and self.state == None:
                    raise ValueError("If level is 'state' or 'county', state cannot be empty")
                
                if self.product == 'csv' and self.year not in range(self.mincompleteyr, self.maxyr + 1):
                    raise ValueError("Data only available from {} onward.".format(self.mincompleteyr))
                elif self.product == 'xls':
                    if self.level in ['us', 'state'] and self.year not in range(self.minstateyr, self.maxyr + 1):
                        raise ValueError("Data only available from {} onward.".format(self.mincompleteyr))
                    if self.level == 'county' and self.year not in range(self.mincountyyr, self.maxyr + 1):
                        raise ValueError("Data only available from {} onward.".format(self.minstateyr))
                        raise ValueError("Data only available from {} onward.".format(self.mincountyyr))

                if self.state != None and self.state not in self.statenumbers:
                    raise ValueError("state must represent two digit state abbreviation")

    def get_table(self):
        """
        Downloads data from IRS SOI Tax Stats Historical Tables
        """
        if self.table != "2":
            filename = "histab" + self.table + '.xls'
        else:
            if self.product == 'csv':
                filename = "{}in54cmcsv.csv".format(self.yy)
            
            elif self.product == 'xls':
                # need us, state, county, and one with us + state
                if self.level in '*':
                    filename = "{}in54cm.xlsx".format(self.yy)
                
                elif self.level in ['state', 'us']:
                    filename = "{}in{}{}.xls".format(self.yy, self.stnum, self.state)
            
                elif self.level == 'county':
                    if self.state == None:
                        filename = "{}incyall.xls".format(self.yy)
                    else:
                        filename = "{}incy{}.xls".format(self.yy, self.state)
            
        urlstub = 'https://www.irs.gov/pub/irs-soi/'
        
        url = urlstub + filename
        urllib.request.urlretrieve(url, filename)
        return filename
    
    def get_docs(self):
        """
        Downloads documentation associated with IRS SOI Historical Table 2
        """
        
        if self.year < self.mincompleteyr:
            raise ValueError("Documentation only available 2012 and onwards.")

        filename = '{}incmdocguide'.format(self.yy)
        urlstub = 'https://www.irs.gov/pub/irs-soi/'
        url = urlstub + filename + ".doc"
        urllib.request.urlretrieve(url, filename + ".doc")
        return filename