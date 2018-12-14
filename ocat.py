
server = "cda.harvard.edu"
service = "srservices/ocatDetails.do"
resource = "https://{0}/{1}".format(server, service)

OCAT_TO_HUMAN = {
    'SEQ_NUM' : 'Sequence Number',
    'STATUS' : 'Observation Status',  # Archived, Observed, Scheduled
    'OBSID' : 'OBS_ID',
    'PR_NUM' : 'Proposal Number',
    'TARGET_NAME' : 'Target Name',
    'GRID_NAME' : '',
    'INSTR' : 'Instrument',
    'GRAT' : 'Grarting',
    'TYPE' : '',                      ##  <<<< TODO: ??
    'OBS_CYCLE' : 'Observation Cycle',
    'PROP_CYCLE' : 'Propoal Planning Cycle',
    'CHARGE_CYCLE' : 'Change Time Cycle',
    'START_DATE' : 'DATE-OBS',
    'PUBLIC_AVAIL' : 'Publicly available',
    'READOUT_DETECTOR' : 'Readout Detector',  ## <<<< CHECK
    'DATAMODE' : 'DATAMODE',   ## <<< CHECK (or really READMODE?)
    'JOINT' : 'Joint Proposal Awarded Time on Other Facilities?',  
    'HST' : '',
    'NOAO' : '',
    'NRAO' : '',
    'RXTE' : '',
    'SPITZER' : '',
    'SUZAKU' : '',
    'XMM' : '',
    'SWIFT' : '',
    'NUSTAR' : '',
    'CATEGORY' : 'Object Classification',
    'SEG_MAX_NUM' : 'Maximum number of observation segments',   ## <<< CHECK
    'PROP_TITLE' : 'Proposal Title',
    'PI_NAME' : 'Principal Investigator',
    'OBSERVER' : 'Observer',
    'APP_EXP' : 'Approved Exposure Time',
    'EXP_TIME' : 'Actual Exposure Time',
    'RA' : 'Right Ascention (J2000)',
    'Dec' : 'Declination (J2000)',
    'SOE_ROLL' : 'Scheduled Roll',
    'TIME_CRIT' : 'Is this a time critical observation?',
    'Y_OFF' : '',
    'Z_OFF' : '',
    'X_SIM' : '',
    'Z_SIM' : '',
    'RASTER' : '',
    'OBJ_TYPE' : '',  # <<< CHECK SSO object
    'OBJ' : '',    # <<< SSO 
    'NUDGE' : '',
    'PHOTO' : '',   
    'VMAG' : 'Estimate V magnitude of target',
    'EST_CNT_RATE' : 'Estimated count rate',
    'FORDER_CNT_RATE' : 'First Order count rate',
    'COUNT_RATE' : 'Observed count rate (L2 events)',
    'EVENT_COUNT' : 'Observed number of counts (L2 events)',
    'DITHER' : 'Speical dither requested?',
    'Y_AMP' : '',
    'Y_FREQ' : '',
    'Y_PHASE' : '',
    'Z_AMP' : '',
    'Z_FREQ' : '',
    'Z_PHASE' : '',
    'ROLL' : 'Does this observation have a ROLL contraint?',
    'WINDOW' : 'Does this observatio have a temporal window contraint?',
    'UNINT' : 'Does this observation have to happen uninterrupted',
    'MONITOR' : 'Is this observation part of a monitor sequence',
    'PRE_ID' : 'Previous obsid in the monitor sequence',
    'MON_MIN' : 'Min lag from pervious',
    'MON_MAX' : 'Max lag from previous',
    'GROUP_ID' : '',
    'CONSTR' : '',
    'EPOCH' : 'T0 for phase contraint',
    'PERIOD' : '',
    'PSTART' : 'period start',
    'PS_MARG' : 'period start margin',
    'PEND' : 'period end',
    'PE_MARG' : 'period end marging',
    'MULTITEL' : '',
    'MULTITEL_OBS' : '',
    'MULTITEL_INT' : '',
    'CONSTR_RMK' : '',
    'TOO_TYPE' : '',
    'TOO_START' : '',
    'TOO_STOP' : '',
    'ALT_GROUP' : '',
    'ALT_TRIG' : '',
    'SIMODE' : '',
    'HRC' : '',
    'SPECT_MODE' : '',
    'BLANK_EN' : '',
    'U_HI' : '',
    'V_HI' : '',
    'U_LO' : '',
    'V_LO' : '',
    'TIMING' : '',
    'Z_BLK' : '',
    'ACIS' : '',
    'MODE' : '',
    'BEP_PACK' : '',
    'DROPPED_CHIP_CNT' : '',
    'I0' : '',
    'I1' : '',
    'I2' : '',
    'I3' : '',
    'S0' : '',
    'S1' : '',
    'S2' : '',
    'S3' : '',
    'S4' : '',
    'S5' : '',
    'SPECTRA_MAX_COUNT' : '',
    'MULTIPLE_SPECTRAL_LINES' : '',
    'SUBARY' : '',
    'STRT_ROW' : '',
    'ROW_CNT' : '',
    'D_CYC' : '',
    'SEC_CNT' : '',
    'PR_TIME' : '',
    'SEC_TIME' : '',
    'F_TIME' : '',
    'OC_SUM' : '',
    'OC_ROW' : '',
    'OC_COL' : '',
    'EVFIL' : '',
    'EVFIL_LO' : '',
    'EVFIL_RA' : '',
    'EFFICIENT' : '',
    'SPWIN' : ''
    }
  



#import ciao_contrib.logger_wrapper as lw
#logger= lw.initialize_module_logger("cda.ocat")

#verb0 = logger.verbose0
#verb1 = logger.verbose1
#verb2 = logger.verbose2
#verb3 = logger.verbose3
#verb4 = logger.verbose4
#verb5 = logger.verbose5


def make_URL_request( resource, vals ):
    """
    Query and retrieve results from resourse using dictionary of
    vals values.
    """
    import urllib as urllib
    import urllib2 as urllib2

    #verb5( "Querying resource " + resource )
    #verb5( "with parameters" + str( vals ) )

    params = urllib.urlencode( vals )  # Encode into URL string, escape stuff/etc.
    request = urllib2.Request( resource, params )
    #request.add_header('User-Agent', 'ciao_contrib.cda.csccli/1.0') #make easy to ID in logs
    response = urllib2.urlopen( request )
    page = response.read()
    
    if len(page) == 0:
        raise Exception("Problem accessing resource {0}".format(resource))
    
    #verb5( "URL Code: {0}".format( response.getcode() ))
    if response.getcode() != 200:
        raise Exception( page )
    
    return page



for oo in [315, 1838]: #[ 14695, 14696,15542, 15638, 15543, 15544 ]:

  page = make_URL_request( resource, { "obsid" : oo, "format" : "text" } )


  page_lines = page.split("\n")

  page_lines_nohdr = filter( lambda x : not x.startswith("#"), page_lines )

  hdr = page_lines_nohdr[0].split("\t")
  tab = []
  for ln in page_lines_nohdr[2:]:
      tlin = ln.replace("\t\t","\tNone\t")
      flds = tlin.split("\t")
      tab.append( dict(zip( hdr, flds)))
    
  print tab




