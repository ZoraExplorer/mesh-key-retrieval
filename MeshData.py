# Mesh Keys


class Taskslist:
    def region_api_selec(site,region_selection):
        data = {
            "footpatrol": 
    
            {
                'gb':{"key":"253ae55594","secret":"33367a7dc65731b695e0882f12d5f707","apikey":"52F096E285134DF2A9E1AFAF979BB415"},
         
                'fr':{"key":"9100705ee0","secret":"b6b631e9c6866ad0fb654e29bcd22b7c","apikey":"536AE78F060D458F8342241C6A2A7190"},

                'nl':{"key":"253ae55594","secret":"b6b631e9c6866ad0fb654e29bcd22b7c","apikey":"6986D83D7D8F4AD7A736852B9FBDB0D6"},

                'ie':{"key":"253ae55594","secret":"b6b631e9c6866ad0fb654e29bcd22b7c","apikey":"6986D83D7D8F4AD7A736852B9FBDB0D6"},

                'sg':{"key":"253ae55594","secret":"33367a7dc65731b695e0882f12d5f707","apikey":"52F096E285134DF2A9E1AFAF979BB415"},

                'se':{"key":"253ae55594","secret":"b6b631e9c6866ad0fb654e29bcd22b7c","apikey":"6986D83D7D8F4AD7A736852B9FBDB0D6"}
         
             },  

             'jdsports':  

             {
                 'gb':{"key": "d1bdff50c5","secret": "3442497330233aecfe132ddfbbd4d46d","apikey": "4CE1177BB983470AB15E703EC95E5285"},

                 'ie':{"key": "d3cbd87f10","secret": "3c279838fd48cf45a397898344eedad8","apikey": "451FE27E0BD544C4B07C395CD5888547"},

                 'fr':{"key": "f2188a5b06","secret": "8bb6bd51c83f2ec9821e1bda5c77b25b","apikey": "B3B51B56ADC34016A6FEF7F8C337B836"},

                 'nl':{"key": "6805a9f237","secret": "60f38ccd64b72be47eef4638edb489ae","apikey": "9D93C082EA864FF5884FD4763B856C6D"},

                 'es':{"key": "a15e99c07a","secret": "364e1006ccf7959fc33ce5eef9486bbe","apikey": "EB396335754A48D795BB903B49E3AD91"},

                 'de':{"key": "3d44230df4","secret": "f266ed9166db7af4351fa88841b8c300","apikey": "195F25A2910341CBA49535BC5941F445"},

                 'it':{"key": "3dc77f7e7f","secret": "089587c2316656881bbf17661bbf0d33","apikey": "7B6B83F76BAA41DDB90D4147FB3D3C63"},

                 'se':{"key": "9ea5ecdfaa","secret": "80a73c56e06ef76337c6efaf94460b78","apikey": "69A3F58BA52C4DB88CB5585707A3C0F4"},

                 'dk':{"key": "d094b9a365","secret": "7144518ade2e82ca6385561dcc02b383","apikey": "00B2CE710BD64AC2AD7A34FEB2A7B296"},

                 'be':{"key": "c4fb0734be","secret": "ef9a27be3268cdbc3240ae643b32a4fa","apikey": "61100D5FA36F4F248D5DE6D546D47921"},

                 'au':{"key": "60122c4543","secret": "066268d08e45b34290f553f9f4e56906","apikey": "1753F69D6B4F48F9956DEE1002A83491"},

                 'at':{"key": "60122c4543","secret": "066268d08e45b34290f553f9f4e56906","apikey": "23E9D73FA2A64957BA367515970333A4"},

                 'fi':{"key": "2a31c0c80f","secret": "8a2efdb8e9d5a6d081884e3d334abcc6","apikey": "D8F6CCA07E3549348647B8DE8AA6E9D5"},

                 'sg':{"key": "94e8c7ae06","secret": "cf4205cb322026a0e120f63dcdece0f4","apikey": "1447E7A429A54DCB80E03D56EF6924DC"},

                 'pt':{"key": "54c90d126d","secret": "236a4ef99afaeb06cf1023586f0ae41b","apikey": "85675FFA06A6462CACCF241DA705A6A0"}
         
              },

             'size':

             {
                 'gb':{"key": "fbc28a16ec","secret": "d7c7872a58138c995430dd957b18c85b","apikey": "9039BF1C29724461881ACD80232F5313"},

                 'nl':{"key": "42d159adbc","secret": "fa796f80ae3a9790b1796e491fa19ced","apikey": "509EF36F9882470089AACAC99135B9CB"},

                 'de':{"key": "9242ac82fe","secret": "1c2962f6f2e346c0165e43726176fc7b","apikey": "B9AB7B6B5CD74497A4C2348F5F5E89F7"},

                 'fr':{"key": "2a54a4bd66","secret": "b64d50a93b0c907c109b29fa9b3ca5a2","apikey": "59DCF6F765D346619E3409F1F1FE7D10"},

                 'es':{"key": "b1a7868a8c","secret": "5679a7c7f8cb13d58253625a81bca52b","apikey": "907108D8F6754F588927ED81B37D2E05"},

                 'it':{"key": "138d698519","secret": "9acd9eecc04be281930c8b16f143e4b0","apikey": "D0C9A901F06A4C7AA00FAD92B0783C64"},

                 'se':{"key": "782bdb38d8","secret": "fa7827cc513e9fe843be12124d013b25","apikey": "A99C7C5147414D58BFEBDC58D2DF9A95"},

                 'dk':{"key": "6af2364998","Secret": "6f81172915d84691817dd22040f0b4f9","apikey": "4E728C6150EE4396A8BACB0DD627DA2F"},

                 'ie':{"key": "a3c0389e3d","Secret": "2df03a2387ea458a25df9b609b09a972","apikey": "4422119FE17E4F5B8E775B32673DDB64"}
         
             }
        
        }

        try:
            return data[site][region_selection]
        except:
            return None




