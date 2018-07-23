#
#


def calcPot(radius, type, H, P, p, n):
    sum = 0.0;

    if(radius == '7A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.357230 #0.488487;
            for i in range(0, P):
                sum += 0.076624 #0.067881;
            for i in range(0, p):
                sum += -0.170862 #-0.323076;
            for i in range(0, n):
                sum += -0.193105 #-0.341626;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.076624 #0.067881;
            for i in range(0, P):
                sum += -0.185727 #-0.397028;
            for i in range(0, p):
                sum += -0.540692 #-0.854789;
            for i in range(0, n):
                sum += -0.553291 #-0.942418;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.170862 #-0.323076;
            for i in range(0, P):
                sum += -0.540692 #-0.854789;
            for i in range(0, p):
                sum += -0.837066 #-1.367547;
            for i in range(0, n):
                sum += -0.937943 #-1.563853;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.193105 #-0.341626;
            for i in range(0, P):
                sum += -0.553291 #-0.942418;
            for i in range(0, p):
                sum += -0.937943 #-1.563853;
            for i in range(0, n):
                sum += -0.895086 #-1.507146;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '8A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.340428 #0.475826;
            for i in range(0, P):
                sum += 0.076316 #0.064790;
            for i in range(0, p):
                sum += -0.180578 #-0.333881;
            for i in range(0, n):
                sum += -0.194497 #-0.350033;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.076316 #0.064790;
            for i in range(0, P):
                sum += -0.174533 #-0.386490;
            for i in range(0, p):
                sum += -0.523907 #-0.837680;
            for i in range(0, n):
                sum += -0.546583#-0.919767;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.180578 #-0.333881;
            for i in range(0, P):
                sum += -0.523907 #-0.837680;
            for i in range(0, p):
                sum += -0.816761 #-1.337451;
            for i in range(0, n):
                sum += -0.928537 #-1.535952;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.194497 #-0.350033;
            for i in range(0, P):
                sum += -0.546583 #-0.919767;
            for i in range(0, p):
                sum += -0.928537 #-1.535952;
            for i in range(0, n):
                sum += -0.880363 #-1.451336;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '9A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.327777 #0.453268;
            for i in range(0, P):
                sum += 0.070114 #0.052530;
            for i in range(0, p):
                sum += -0.184261 #-0.332153;
            for i in range(0, n):
                sum += -0.183928 #-0.338976;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.070114 #0.052530;
            for i in range(0, P):
                sum += -0.169004 #-0.366313;
            for i in range(0, p):
                sum += -0.505871 #-0.825331;
            for i in range(0, n):
                sum += -0.539249 #-0.899374;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.184261 #-0.332153;
            for i in range(0, P):
                sum += -0.505871 #-0.825331;
            for i in range(0, p):
                sum += -0.836627 #-1.322456;
            for i in range(0, n):
                sum += -0.902965 #-1.499179;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.183928 #-0.338976;
            for i in range(0, P):
                sum += -0.539249 #-0.899374;
            for i in range(0, p):
                sum += -0.902965 #-1.499179;
            for i in range(0, n):
                sum += -0.902544 #-1.433728;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
        
    elif(radius == '10A'):
        if (type == 'H'):
            for i in range(0, H):
                        # ver_ultimate; ver_final; ver_qt; ver_new; ver_6; ver_5;  ver_4; ver_3; ver_2; ver_1, ver_October
                sum += 0.475037 #0.375094 #0.333095 #0.387099 #0.240239 #0.211227 #0.238415 #0.303159 #0.238990 #0.309556 #0.435946;
            for i in range(0, P):
                sum += 0.038555 #0.058151 #0.047514 #0.062142 #0.053656 #0.036154 #0.053411 #0.113197 #0.053223 #0.067102 #0.046302;
            for i in range(0, p):
                sum += -0.144155 #-0.085803 #-0.081367 #-0.102275 #-0.155074 #-0.147022 #-0.153545 #-0.157932 #-0.153766 #-0.188736 #-0.328980;
            for i in range(0, n):
                sum += -0.261464 #-0.203857 #-0.181453 #-0.223264 #-0.172359 #-0.139277 #-0.170240 #-0.134649 #-0.169946 #-0.179998 #-0.33622;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.038555 #0.058151 #0.047514 #0.062142 #0.053656 #0.036154 #0.053411 #0.113197 #0.053223 #0.067102 #0.046302;
            for i in range(0, P):
                sum += -0.404414 #-0.258404 #-0.266024 #-0.270518 #-0.161026 #-0.179655 #-0.156421 #-0.057010 #-0.156863 #-0.164721 #-0.364340;
            for i in range(0, p):
                sum += -0.634483 #-0.468914 #-0.454882 #-0.496353 #-0.441194 #-0.426037 #-0.437075 #-0.418822 #-0.437517 #-0.494455 #-0.814426;
            for i in range(0, n):
                sum += -0.795003 #-0.600509 #-0.571430 #-0.655455 #-0.482182 #-0.452103 #-0.482048 #-0.410788 #-0.482361 #-0.527023 #-0.871019;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.144155 #-0.085803 #-0.081367 #-0.102275 #-0.155074 #-0.147022 #-0.153545#-0.157932 #-0.153766 #-0.188736 #-0.328980;
            for i in range(0, P):
                sum += -0.634483 #-0.468914 #-0.454882 #-0.496353 #-0.441194 #-0.426037 #-0.437075#-0.418822 #-0.437517 #-0.494455 #-0.814426;
            for i in range(0, p):
                sum += -0.761091 #-0.748200 #-0.699428 #-0.808914 #-0.735038 #-0.701821 #-0.740165 #-0.891226 #-0.740607 #-0.825508 #-1.333656;
            for i in range(0, n):
                sum += -0.980940 #-0.849122 #-0.793877 #-0.953323 #-0.822826#-0.756799 #-0.818326 #-0.824777 #-0.818000 #-0.885295 #-1.455513;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.261464 #-0.203857 #-0.181453 #-0.223264 #-0.172359 #-0.139277 #-0.170240 #-0.134649 #-0.169946 #-0.179998 #-0.336223;
            for i in range(0, P):
                sum += -0.795003 #-0.600509 #-0.571430 #-0.655455 #-0.482182 #-0.452103 #-0.482048 #-0.410788 #-0.482361 #-0.527023 #-0.871019;
            for i in range(0, p):
                sum += -0.980940 #-0.849122 #-0.793877 #-0.953323 #-0.822826 #-0.756799 #-0.818326 #-0.824777 #-0.818000 #-0.885295 #-1.455513;
            for i in range(0, n):
                sum += -1.108522 #-0.940419 #-0.899644 #-1.098303 #-0.817212 #-0.760309 #-0.826452 #-0.761754 #-0.826894 #-0.889501 #-1.419626;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '11A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.473385 #0.383079 #0.341026#0.394128 #0.243201 #0.214395 #0.241859 #0.302206 #0.242364 #0.308382 #0.433586;
            for i in range(0, P):
                sum += 0.038643 #0.065033 #0.054648 #0.069393 #0.053893 #0.036746 #0.054567 #0.114499 #0.054348 #0.067675 #0.045205;
            for i in range(0, p):
                sum += -0.147918 #-0.096206 #-0.093972 #-0.110240 #-0.155534 #-0.147817 #-0.153517 #-0.157212 #-0.153647 #-0.186406 #-0.333059;
            for i in range(0, n):
                sum += -0.257153 #-0.192444 #-0.171078 #-0.215253#-0.171183 #-0.142373 #-0.171004 #-0.131142 #-0.170710 #-0.179441 #-0.333059;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.038643 #0.065033 #0.054648 #0.069393 #0.053893 #0.036746 #0.054567 #0.114499 #0.054348 #0.067675 #0.045205;
            for i in range(0, P):
                sum += -0.407035 #-0.272483 #-0.277831 #-0.283847 #-0.161315 #-0.180651 #-0.157210 #-0.066438 #-0.157632 #-0.166830 #-0.366558;
            for i in range(0, p):
                sum += -0.633994 #-0.471129 #-0.453624 #-0.503876 #-0.428452 #-0.412480 #-0.425372 #-0.417394 #-0.425794 #-0.488858 #-0.814336;
            for i in range(0, n):
                sum += -0.787794 #-0.614191 #-0.586021 #-0.664971 #-0.480684 #-0.450437 #-0.480960 #-0.412384 #-0.481175#-0.519853 #-0.861217;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.147918 #-0.096206 #-0.093972 #-0.110240 #-0.155534#-0.147817 #-0.153517 #-0.157212 #-0.153647 #-0.186406 #-0.333059;
            for i in range(0, P):
                sum += -0.633994 #-0.471129 #-0.453624 #-0.503876 #-0.428452 #-0.412480 #-0.425372 #-0.417394 #-0.425794 #-0.488858 #-0.814336;
            for i in range(0, p):
                sum += -0.778418 #-0.753313 #-0.705171 #-0.806845 #-0.712257 #-0.675820 #-0.714974 #-0.865590 #-0.715397 #-0.820257 #-1.362225;
            for i in range(0, n):
                sum += -0.966598 #-0.872787 #-0.820788 #-0.977352 #-0.811247#-0.744362 #-0.804550 #-0.815465 #-0.804163 #-0.869467 #-1.445574;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.257153 #-0.192444 #-0.171078 #-0.215253 #-0.171183 #-0.142373 #-0.171004 #-0.131142 #-0.170710 #-0.179441 #-0.333778;
            for i in range(0, P):
                sum += -0.787794 #-0.614191 #-0.586021 #-0.664971 #-0.480684 #-0.450437 #-0.480960 #-0.412384 #-0.481175 #-0.519853 #-0.861217;
            for i in range(0, p):
                sum += -0.966598 #-0.872787 #-0.820788 #-0.977352 #-0.811247 #-0.744362 #-0.804550 #-0.815465 #-0.804163 #-0.869467 #-1.445574;
            for i in range(0, n):
                sum += -1.108191 #-0.925898 #-0.883822 #-1.062325 #-0.827245 #-0.761815 #-0.834677 #-0.773669 #-0.834561 #-0.873333 #-1.434046;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '12A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.466396  #0.382330 #0.341703 #0.392413 #0.238553 #0.210319 #0.237769 #0.289144 #0.238146 #0.300254 #0.427054;
            for i in range(0, P):
                sum += 0.034656 #0.070420 #0.058219 #0.073956 #0.054798 #0.037291 #0.054648 #0.116393 #0.054428 #0.066214 #0.043497;
            for i in range(0, p):
                sum += -0.145785 #-0.094535 #-0.093727 #-0.108566 #-0.155914 #-0.148092 #-0.154412 #-0.156935 #-0.154508 #-0.188776 #-0.330881;
            for i in range(0, n):
                sum += -0.253824 #-0.189925 #-0.170336 #-0.212181 #-0.176803 #-0.149081 #-0.176758 #-0.131211 #-0.176317 #-0.183741 #-0.332487;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.034656 #0.070420 #0.058219 #0.073956 #0.054798 #0.037291 #0.054648 #0.116393 #0.054428 #0.066214 #0.043497;
            for i in range(0, P):
                sum += -0.408104 #-0.279752 #-0.287157 #-0.288582 #-0.151473 #-0.170232 #-0.146979 #-0.066876 #-0.147420 #-0.153873 #-0.363226;
            for i in range(0, p):
                sum += -0.622360 #-0.469096 #-0.451357 #-0.500641 #-0.415833 #-0.399890 #-0.412388 #-0.408759 #-0.412829 #-0.475475 #-0.801509;
            for i in range(0, n):
                sum += -0.777421 #-0.613698 #-0.584122 #-0.662628 #-0.461089 #-0.430405 #-0.461142 #-0.399623 #-0.461411 #-0.505904 #-0.843447;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.145785 #-0.094535 #-0.093727 #-0.108566 #-0.155914 #-0.148092 #-0.154412 #-0.156935 #-0.154508 #-0.188776 #-0.330881;
            for i in range(0, P):
                sum += -0.622360 #-0.469096 #-0.451357 #-0.500641 #-0.415833 #-0.399890 #-0.412388 #-0.408759 #-0.412829 #-0.475475 #-0.801509;
            for i in range(0, p):
                sum += -0.776532 #-0.731580 #-0.681384 #-0.789031 #-0.706595 #-0.667740 #-0.706537 #-0.865398 #-0.706978 #-0.812723 #-1.354344;
            for i in range(0, n):
                sum += -0.953496 #-0.871710 #-0.812978 #-0.975530 #-0.798633 #-0.732412 #-0.792648 #-0.807726 #-0.792407 #-0.856199 #-1.433149;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.253824 #-0.189925 #-0.170336 #-0.212181 #-0.176803 #-0.149081 #-0.176758 #-0.131211 #-0.176317 #-0.183741 #-0.332487;
            for i in range(0, P):
                sum += -0.777421 #-0.613698 #-0.584122 #-0.662628 #-0.461089 #-0.430405 #-0.461142 #-0.399623 #-0.461411 #-0.505904 #-0.843447;
            for i in range(0, p):
                sum += -0.953496 #-0.871710 #-0.812978 #-0.975530 #-0.798633 #-0.732412 #-0.792648 #-0.807726 #-0.792407 #-0.856199 #-1.433149;
            for i in range(0, n):
                sum += -1.108452 #-0.926632 #-0.885243 #-1.059737 #-0.813558 #-0.748858 #-0.818670 #-0.756571 #-0.818226 #-0.863322 #-1.423892;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
            
    elif(radius == '13A'):
        if (type == 'H'):
            for i in range(0, H):
                #    ver_new; ver_1; ver_October
                sum += 0.393366 #0.292721 #0.416419;
            for i in range(0, P):
                sum += 0.072570 #0.063739 #0.040430;
            for i in range(0, p):
                sum += -0.110311 #-0.183246 #-0.328377;
            for i in range(0, n):
                sum += -0.201332 #-0.182141 #-0.323056;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.072570 #0.063739 #0.040430;
            for i in range(0, P):
                sum += -0.288051 #-0.150046 #-0.359538;
            for i in range(0, p):
                sum += -0.500064 #-0.471339 #-0.787919;
            for i in range(0, n):
                sum += -0.660913 #-0.494148 #-0.826608;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.110311 #-0.183246 #-0.328377;
            for i in range(0, P):
                sum += -0.500064 #-0.471339 #-0.787919;
            for i in range(0, p):
                sum += -0.782550 #-0.817420 #-1.358547;
            for i in range(0, n):
                sum += -0.962501 #-0.845679 #-1.412884;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.201332 #-0.182141 #-0.323056;
            for i in range(0, P):
                sum += -0.660913 #-0.494148 #-0.826608;
            for i in range(0, p):
                sum += -0.962501 #-0.845679 #-1.412884;
            for i in range(0, n):
                sum += -1.073209 #-0.852660 #-1.391926;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '14A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.388657 #0.286721 #0.404853;
            for i in range(0, P):
                sum += 0.075686 #0.064229 #0.040143;
            for i in range(0, p):
                sum += -0.110308 #-0.180956 #-0.321375;
            for i in range(0, n):
                sum += -0.197199 #-0.183380 #-0.316476;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.075686 #0.064229 #0.040143;
            for i in range(0, P):
                sum += -0.288411 #-0.147226 #-0.354339;
            for i in range(0, p):
                sum += -0.492379 #-0.465964 #-0.776806;
            for i in range(0, n):
                sum += -0.640217 #-0.484786 #-0.807298;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.110308 #-0.180956 #-0.321375;
            for i in range(0, P):
                sum += -0.492379 #-0.465964 #-0.776806;
            for i in range(0, p):
                sum += -0.776388 #-0.809961 #-1.345226;
            for i in range(0, n):
                sum += -0.942916 #-0.837288 #-1.391022;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.197199 #-0.183380 #-0.316476;
            for i in range(0, P):
                sum += -0.640217 #-0.484786 #-0.807298;
            for i in range(0, p):
                sum += -0.942916 #-0.837288 #-1.391022;
            for i in range(0, n):
                sum += -1.071630 #-0.847306 #-1.377095;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '15A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.387474 #0.281034 #0.390032;
            for i in range(0, P):
                sum += 0.076762 #0.062730 #0.040391;
            for i in range(0, p):
                sum += -0.111589 #-0.175204 #-0.314503;
            for i in range(0, n):
                sum += -0.196151 #-0.181695 #-0.307517;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.076762 #0.062730 #0.040391;
            for i in range(0, P):
                sum += -0.295850 #-0.147428 #-0.348285;
            for i in range(0, p):
                sum += -0.492790 #-0.458911 #-0.762838;
            for i in range(0, n):
                sum += -0.624713#-0.474361 #-0.787479;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.111589 #-0.175204 #-0.314503;
            for i in range(0, P):
                sum += -0.492790 #-0.458911 #-0.762838;
            for i in range(0, p):
                sum += -0.760169 #-0.801887 #-1.338053;
            for i in range(0, n):
                sum += -0.929303 #-0.825456 #-1.377834;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.196151 #-0.181695 #-0.307517;
            for i in range(0, P):
                sum += -0.624713#-0.474361 #-0.787479;
            for i in range(0, p):
                sum += -0.929303 #-0.825456 #-1.377834;
            for i in range(0, n):
                sum += -1.049547 #-0.829656 #-1.356265;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '16A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.276599 #0.363487;
            for i in range(0, P):
                sum += 0.062277 #0.043263;
            for i in range(0, p):
                sum += -0.173152 #-0.312802;
            for i in range(0, n):
                sum += -0.179610 #-0.296845;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.062277 #0.043263;
            for i in range(0, P):
                sum += -0.148358 #-0.311172;
            for i in range(0, p):
                sum += -0.450825 #-0.727724;
            for i in range(0, n):
                sum += -0.463060 #-0.736081;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.173152 #-0.312802;
            for i in range(0, P):
                sum += -0.450825 #-0.727724;
            for i in range(0, p):
                sum += -0.799167 #-1.307606;
            for i in range(0, n):
                sum += -0.818918 #-1.304541;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.179610 #-0.296845;
            for i in range(0, P):
                sum += -0.463060 #-0.736081;
            for i in range(0, p):
                sum += -0.818918 #-1.304541;
            for i in range(0, n):
                sum += -0.829892 #-1.275122;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '17A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.272420 #0.356920;
            for i in range(0, P):
                sum += 0.061117 #0.042913;
            for i in range(0, p):
                sum += -0.169652 #-0.308535;
            for i in range(0, n):
                sum += -0.178319 #-0.290723;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.061117 #0.042913;
            for i in range(0, P):
                sum += -0.146014 #-0.309476;
            for i in range(0, p):
                sum += -0.444021 #-0.719899;
            for i in range(0, n):
                sum += -0.459501 #-0.720508;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.169652 #-0.308535;
            for i in range(0, P):
                sum += -0.444021 #-0.719899;
            for i in range(0, p):
                sum += -0.797987 #-1.303305;
            for i in range(0, n):
                sum += -0.816580 #-1.283040;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.178319 #-0.290723;
            for i in range(0, P):
                sum += -0.459501 #-0.720508;
            for i in range(0, p):
                sum += -0.816580 #-1.283040;
            for i in range(0, n):
                sum += -0.828559 #-1.265493;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '18A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.268598 #0.349901;
            for i in range(0, P):
                sum += 0.060223 #0.042061;
            for i in range(0, p):
                sum += -0.169954 #-0.307099;
            for i in range(0, n):
                sum += -0.177170 #-0.286694;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.060223 #0.042061;
            for i in range(0, P):
                sum += -0.141235 #-0.301136;
            for i in range(0, p):
                sum += -0.441063 #-0.708865;
            for i in range(0, n):
                sum += -0.457726 #-0.708564;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.169954 #-0.307099;
            for i in range(0, P):
                sum += -0.441063 #-0.708865;
            for i in range(0, p):
                sum += -0.793502 #-1.294795;
            for i in range(0, n):
                sum += -0.810237 #-1.271084;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.177170 #-0.286694;
            for i in range(0, P):
                sum += -0.457726 #-0.708564;
            for i in range(0, p):
                sum += -0.810237 #-1.271084;
            for i in range(0, n):
                sum += -0.832905 #-1.247778;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '19A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.263885 #0.359669;
            for i in range(0, P):
                sum += 0.059369 #0.034803;
            for i in range(0, p):
                sum += -0.167705 #-0.305078;
            for i in range(0, n):
                sum += -0.176773 #-0.283355;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.059369 #0.034803;
            for i in range(0, P):
                sum += -0.141332 #-0.328390;
            for i in range(0, p):
                sum += -0.439541 #-0.729192;
            for i in range(0, n):
                sum += -0.452153 #-0.731418;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.167705 #-0.305078;
            for i in range(0, P):
                sum += -0.439541 #-0.729192;
            for i in range(0, p):
                sum += -0.791685 #-1.323347;
            for i in range(0, n):
                sum += -0.806666 #-1.307416;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.176773 #-0.283355;
            for i in range(0, H):
                sum += -0.452153 #-0.731418;
            for i in range(0, p):
                sum += -0.806666 #-1.307416;
            for i in range(0, n):
                 sum += -0.820460 #-1.280113;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '20A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.260313 #0.353219;
            for i in range(0, P):
                sum += 0.057891 #0.033431;
            for i in range(0, p):
                sum += -0.168566 #-0.302485;
            for i in range(0, n):
                sum += -0.174853 #-0.279591;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.057891 #0.033431;
            for i in range(0, P):
                sum += -0.138513 #-0.324690;
            for i in range(0, p):
                sum += -0.437759 #-0.718757;
            for i in range(0, n):
                sum += -0.448410 #-0.718937;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.168566 #-0.302485;
            for i in range(0, P):
                sum += -0.437759 #-0.718757;
            for i in range(0, p):
                sum += -0.783440 #-1.311192;
            for i in range(0, n):
                sum += -0.797740 #-1.291898;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.174853 #-0.279591;
            for i in range(0, P):
                sum += -0.448410 #-0.718937;
            for i in range(0, p):
                sum += -0.797740 #-1.291898;
            for i in range(0, n):
                sum += -0.825473 #-1.268799;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        else:
            return sum;
    
    elif(radius == '21A'):
        if (type == 'H'):
            for i in range(0, H):
                sum += 0.258353 #0.347924;
            for i in range(0, P):
                sum += 0.057810 #0.031721;
            for i in range(0, p):
                sum += -0.166872 #-0.300360;
            for i in range(0, n):
                sum += -0.174446#-0.274124;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == 'P'):
            for i in range(0, H):
                sum += 0.057810 #0.031721;
            for i in range(0, P):
                sum += -0.137052 #-0.322981;
            for i in range(0, p):
                sum += -0.437012 #-0.712301;
            for i in range(0, n):
                sum += -0.446600#-0.709973;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '+'):
            for i in range(0, H):
                sum += -0.166872 #-0.300360;
            for i in range(0, P):
                sum += -0.437012 #-0.712301;
            for i in range(0, p):
                sum += -0.786200 #-1.307172;
            for i in range(0, n):
                sum += -0.797917 #-1.282639;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
        
        elif (type == '-'):
            for i in range(0, H):
                sum += -0.174446 #-0.274124;
            for i in range(0, P):
                sum += -0.446600 #-0.709973;
            for i in range(0, p):
                sum += -0.797917 #-1.282639;
            for i in range(0, n):
                sum += -0.818141 #-1.250949;
            if ((H+P+p+n) == 0):
                return 0.0;
            else:
                return sum / (H+P+p+n);
       
        else:
            return sum;
        
    return sum;


# --------------- main ---------------

if __name__ == "__main__":
    
    infilename = '/home/tomi/workspace/FinalScom/out_pdbselect_compl_10-12_ultimate.txt'
    infile = open(infilename, 'r')
    outfilename = '/home/tomi/workspace/FinalScom/out_pdbselect_compl_10-12_ultimate_pot.txt'
    outfile = open(outfilename, 'w')
    
    for line in infile:
        line = line.strip();
        if len(line) < 4:
            continue;
        
        array = line.split(" ")
        pdb = array[0]
        chain = array[1]
        number = array[2]
        type = str(array[3])
        aRadius = array[4]
        aH = int(array[5])
        aP = int(array[6])
        ap = int(array[7])
        an = int(array[8])
        bRadius = array[9]
        bH = int(array[10])
        bP = int(array[11])
        bp = int(array[12])
        bn = int(array[13])
        cRadius = array[14]
        cH = int(array[15])
        cP = int(array[16])
        cp = int(array[17])
        cn = int(array[18])
        classif = array[19]
        
        aPotential = 0.0
        bPotential = 0.0
        cPotential = 0.0
        
        aPotential = calcPot(aRadius, type, aH, aP, ap, an)
        bPotential = calcPot(bRadius, type, bH, bP, bp, bn)
        cPotential = calcPot(cRadius, type, cH, cP, cp, cn)
        if(aPotential == 0 or bPotential == 0 or cPotential ==0 ):
            print 'All potentials are zero: ' + pdb + '.pdb ' + chain + ' AA_no.' + number 
        
        outfile.write(pdb + ' ' + chain + ' ' + number + ' ' + type + ' ' + aRadius + ' ' + str(aPotential)
                      + ' ' + bRadius + ' ' + str(bPotential) + ' ' + cRadius + ' ' + str(cPotential) + ' ' + classif + '\n')
    outfile.close()
    infile.close()
    
