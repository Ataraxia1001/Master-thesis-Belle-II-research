import argparse
import basf2_mva

# +
def get_variables():
    
    my_var=[ 'Btag_d1_R2', 'Btag_d1_thrustBm', 'Btag_d1_thrustOm',
 'Btag_d1_cosTBTO' ,'Btag_d1_cosTBz', 'Btag_d1_KSFWVariables_hso00',
 'Btag_d1_KSFWVariables_hso01' ,'Btag_d1_KSFWVariables_hso02',
 'Btag_d1_KSFWVariables_hso03', 'Btag_d1_KSFWVariables_hso04',
 'Btag_d1_KSFWVariables_hso10', 'Btag_d1_KSFWVariables_hso12',
 'Btag_d1_KSFWVariables_hso14' ,'Btag_d1_KSFWVariables_hso20',
 'Btag_d1_KSFWVariables_hso22', 'Btag_d1_KSFWVariables_hso24',
 'Btag_d1_KSFWVariables_hoo0', 'Btag_d1_KSFWVariables_hoo1',
 'Btag_d1_KSFWVariables_hoo2' ,'Btag_d1_KSFWVariables_hoo3',
 'Btag_d1_KSFWVariables_hoo4',
            'Btag_d1_px', 'Btag_d1_py', 'Btag_d1_pz', 'Btag_d1_pt'
    ]
#'Btag_d1_px' 'Btag_d1_py' 'Btag_d1_pz' 'Btag_d1_pt'
    
#       'Btag_d1_R2', 'Btag_d1_thrustOm',
# 'Btag_d1_cosTBTO', 'Btag_d1_cosTBz' ,'Btag_d1_KSFWVariables_hso00',
# 'Btag_d1_KSFWVariables_hso01', 'Btag_d1_KSFWVariables_hso02',
# 'Btag_d1_KSFWVariables_hso03', 'Btag_d1_KSFWVariables_hso04',
# 'Btag_d1_KSFWVariables_hso10', 'Btag_d1_KSFWVariables_hso12',
# 'Btag_d1_KSFWVariables_hso14', 'Btag_d1_KSFWVariables_hso20',
# 'Btag_d1_KSFWVariables_hso22', 'Btag_d1_KSFWVariables_hso24',
# 'Btag_d1_KSFWVariables_hoo0', 'Btag_d1_KSFWVariables_hoo1',
# 'Btag_d1_KSFWVariables_hoo2', 'Btag_d1_KSFWVariables_hoo3',
# 'Btag_d1_KSFWVariables_hoo4'    
    
#'Bsig_d0_R2' , 'Bsig_d0_thrustOm', 'Bsig_d0_cosTBTO',
# 'Bsig_d0_cosTBz', 'Bsig_d0_KSFWVariables_hso00',
# 'Bsig_d0_KSFWVariables_hso01' ,'Bsig_d0_KSFWVariables_hso02',
# 'Bsig_d0_KSFWVariables_hso03', 'Bsig_d0_KSFWVariables_hso04',
# 'Bsig_d0_KSFWVariables_hso10', 'Bsig_d0_KSFWVariables_hso12',
# 'Bsig_d0_KSFWVariables_hso14', 'Bsig_d0_KSFWVariables_hso20',
# 'Bsig_d0_KSFWVariables_hso22', 'Bsig_d0_KSFWVariables_hso24',
# 'Bsig_d0_KSFWVariables_hoo0', 'Bsig_d0_KSFWVariables_hoo1',
# 'Bsig_d0_KSFWVariables_hoo2', 'Bsig_d0_KSFWVariables_hoo3',
# 'Bsig_d0_KSFWVariables_hoo4'


    #ksfw_variables = [f'KSFWVariables{arg}' for arg in ksfw_args]
    #cleo_cones = [f'CleoConeCS{i}' for i in range(1,10)]
   # cs_variables = ['cosThetaCMS','foxWolframR1','foxWolframR2','foxWolframR3','foxWolframR4', 
   #     'sphericity', 'aplanarity',  'thrust', 'thrustAxisCosTheta', 'cosTBTO', 'cosTBz' ]
   # cs_variables += cleo_cones
   # veto_variables = ['mu_0_isFromJpsiMu','mu_1_isFromJpsiMu', 'mu_0_isInD', 'mu_1_isInD', 'isFromJpsiMuRad']
   # kin_variables = ['pCMS', 'mu_0_pCMS', 'mu_1_pCMS','pCMSDaughterSum','pCMSDaughterDiff']
   # lt_variables = ['extraInfoMuPCMS', 'extraInfoEPCMS', 'extraInfoMuCosTheta', 'extraInfoECosTheta']
    #dt_variables = ['DeltaT', 'DeltaTErr']
    #train_variables = ['cosAngleBetweenMomentumAndVertexVectorInXYPlane',
    #    'cosAngleBetweenMomentumAndVertexVector', 'cosToThrustOfEvent',
    #    'missingMass2OfEvent', 'cosThetaBetweenParticleAndNominalB', 'chiProb']
   # train_variables += cs_variables
    #train_variables += m
   # train_variables += kin_variables
    #train_variables += veto_variables
    #train_variables += dt_variables
    
    return my_var


# -

def get_specific_settings(model: str):
    sp = None
    if model == 'fisher':
        sp = basf2_mva.TMVAOptionsClassification()
        sp.m_method = "Fisher"
        sp.m_type = "Fisher"
        sp.m_config = ("H:V:CreateMVAPdfs:VarTransform=N:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10")
        sp.transform2probability = False;
    elif model == 'svm':
        sp = basf2_mva.TMVAOptionsClassification()
        sp.m_method = "SVM"
        sp.m_type = "SVM"
        sp.m_config = ("H:V:VarTransform=N")
        sp.transform2probability = False;
    elif model == 'fbdt':
        sp = basf2_mva.FastBDTOptions() # here we use the FastBDT method
        sp.m_nTrees = 200    # number of trees in the FastBDT forest(200)
        sp.m_nLevels = 3     # depth of the trees(3)
        sp.m_shrinkage = 0.1 # shrinkage during boosting(0.1)
        sp.m_nCuts = 4       # number of cuts for each tree(4)
        sp.transform2probability = False;
    else:
        raise Exception(f'Model {model} is not supported!')
    return sp

def train(trainData: list, testData: list, model: str, 
          tm_variable: str, output_weights_name: str, tree: str='my_ttree'):
    # Global/General options
    go = basf2_mva.GeneralOptions()
    go.m_datafiles = basf2_mva.vector(*trainData)  # training sample
    go.m_treename = tree    # ntuple tree name
    go.m_identifier = output_weights_name      # name of the file with the trianing info
    train_variables = get_variables()
    go.m_variables = basf2_mva.vector(*train_variables) # input variables
    go.m_target_variable = tm_variable # target for training
    go.m_weight_variable = ""
    sp = get_specific_settings(model)
    basf2_mva.teacher(go,sp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script to split train test")
    parser.add_argument('--train', nargs='+', help="Input MC file names for train")
    parser.add_argument('--test', nargs='+', help="Input MC file names for test")
    parser.add_argument('-tm', '--tm_variable', type=str, 
                        default = 'Btag_d1_isSignal', help="TM variable, 'Btag_d1_isSignal'")
    parser.add_argument('-tag','--tag_name', type=str, default='mva', help="Tag name for output files")
    parser.add_argument('-t','--tree', type=str, default='my_ttree', help="Tree to use")
    parser.add_argument('-m', '--model', type=str, default='fbdt', 
                        choices=['fisher', 'fbdt', 'svm'], help="Model to use")
    args = parser.parse_args()

    output_weights_name = f'./{args.model}_{args.tag_name}.xml'

    train(args.train, args.test, args.model, tm_variable=args.tm_variable, 
            output_weights_name=output_weights_name)

    #Btag_d1_isSignal
    
    
    #outputPdf = f'evaluation-{xmlname}.tex'
    #os.system('$BELLE2_RELEASE_DIR/mva/tools/basf2_mva_evaluate.py  -w notebooks/tmp/ '+
    #        f'-id {go.m_identifier} MyTMVAfbdt.xml -tree {go.m_treename} -train {trainData[0]} -data {testData[0]} -out {outputPdf}')
    #os.system('~/code/4leptons/notebooks/tmp/; pdflatex latex.tex; cd ../../')
