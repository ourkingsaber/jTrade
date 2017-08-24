import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages

# import R's utility package
quantmod = rpackages.importr('quantmod')




if __name__ == '__main__':
    # import rpy2
    # print(rpy2.__version__)
    #
    # from rpy2.rinterface import R_VERSION_BUILD
    # print(R_VERSION_BUILD)

    # print(robjects.r['pi'])

    FORD = robjects.r("""getSymbols("F",from="1990-1-1",to="2012-12-31",auto.assign=F""")
    print(FORD)