'''
Maya Dependency Graph plugin that creates a generic node
'''

import sys
import maya.api.OpenMaya as OpenMaya # OpenMaya 2.0
import maya.cmds as cmds
import maya.mel as mel

def maya_useNewAPI():
    '''
    The presence of this function tells Maya use Maya Python API 2.0
    '''
    pass


kPluginNodeName = "MyUselessNode"
kPluginNodeId = OpenMaya.MTypeId( 0x80007 ) #a unique ID (from 0x00000 to 0x7ffff) for our node


class MyNode(OpenMaya.MPxNode):

    #define static attributes as MObjects (in C++ they are also static)
    sampleInAttribute_A     = OpenMaya.MObject()
    sampleInAttribute_B     = OpenMaya.MObject()
    sampleOutAttribute      = OpenMaya.MObject()
    offsetAttr              = OpenMaya.MObject()
    dummyAttr               = OpenMaya.MObject()


    def __init__(self):
        OpenMaya.MPxNode.__init__(self)


    @staticmethod
    def creator():
        '''
        we can define this method outside the class
        '''
        return MyNode()


    @staticmethod
    def initialize():
        '''
        we can define this method outside the class
        Defines the input and output attributes as static vars in our plug-in class
        '''

        #the following function set allows us create numeric attributes (float, int, vector etc...)
        numericAttributeFn = OpenMaya.MFnNumericAttribute()

        #input attributes
        MyNode.sampleInAttribute_A = numericAttributeFn.create( 'inputA', 'iA', OpenMaya.MFnNumericData.k3Float, 1.0)
        numericAttributeFn.writable = True # Input plug (destination in graph connection)
        numericAttributeFn.storable = True # value can be stored in file
        numericAttributeFn.readable = False # this is not Output plug
        numericAttributeFn.hidden = False # we can hide attributes in UI of they are used for some hidden calculations
        numericAttributeFn.keyable = True # Writable + keyable = we can see it in channel editor
        MyNode.addAttribute(MyNode.sampleInAttribute_A)

        MyNode.sampleInAttribute_B = numericAttributeFn.create( 'inputB', 'iB', OpenMaya.MFnNumericData.k3Float, 1.0)
        numericAttributeFn.writable = True
        numericAttributeFn.storable = True
        numericAttributeFn.readable = False
        numericAttributeFn.hidden = False
        numericAttributeFn.keyable = True
        MyNode.addAttribute(MyNode.sampleInAttribute_B)

        MyNode.offsetAttr = numericAttributeFn.create(  'offset', 'ofs', OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttributeFn.writable = True
        numericAttributeFn.storable = True
        numericAttributeFn.readable = False
        numericAttributeFn.hidden = False
        numericAttributeFn.keyable = True
        numericAttributeFn.setMin(-1.0)
        numericAttributeFn.setMax(1.0)
        MyNode.addAttribute(MyNode.offsetAttr)

        #this attribute does not affects any other attrute
        #changing this attribute value doesn't run Compute method
        MyNode.dummyAttr = numericAttributeFn.create( 'dummy', 'dm', OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttributeFn.writable = True
        numericAttributeFn.storable = True
        numericAttributeFn.readable = True
        numericAttributeFn.hidden = False
        numericAttributeFn.keyable = True
        MyNode.addAttribute(MyNode.dummyAttr)

        #output attribute
        MyNode.sampleOutAttribute = numericAttributeFn.create( 'output', 'o', OpenMaya.MFnNumericData.k3Float, 1.0)
        numericAttributeFn.writable = False
        numericAttributeFn.storable = False
        numericAttributeFn.hidden = False
        numericAttributeFn.readable = True # Output plug (source)
        MyNode.addAttribute(MyNode.sampleOutAttribute)

        #Dependencies
        #if sampleInAttribute changes -> sampleOutAttribute must be changed
        MyNode.attributeAffects(MyNode.sampleInAttribute_A, MyNode.sampleOutAttribute)
        MyNode.attributeAffects(MyNode.sampleInAttribute_B, MyNode.sampleOutAttribute)
        MyNode.attributeAffects(MyNode.offsetAttr, MyNode.sampleOutAttribute)


    def compute(self, pPlug, pDataBlock):
        '''
        pPlug: a connection point related to one of our node attributes (input or output)
        pDataBlock: contains the data on which we will base our computations
        '''

        # for every output attr it shoud be a different procedure (elif)
        if pPlug == MyNode.sampleOutAttribute:

            #Get data handles for each attribute
            sampleInDataHandle_A    = pDataBlock.inputValue(MyNode.sampleInAttribute_A)
            sampleInDataHandle_B    = pDataBlock.inputValue(MyNode.sampleInAttribute_B)
            offsetAttrHandle        = pDataBlock.inputValue(MyNode.offsetAttr)
            dummyAttrHandle         = pDataBlock.inputValue(MyNode.dummyAttr)
            sampleOutDataHandle     = pDataBlock.outputValue(MyNode.sampleOutAttribute)

            #extract the actual value from input attr ata handle
            InValue_A   = sampleInDataHandle_A.asFloat3()
            InValue_B   = sampleInDataHandle_B.asFloat3()
            InOffset    = offsetAttrHandle.asFloat()
            InDummy     = dummyAttrHandle.asFloat()

            # === <calculations>
            mVector_A = OpenMaya.MFloatVector(InValue_A[0], InValue_A[1], InValue_A[2])
            mVector_B = OpenMaya.MFloatVector(InValue_B[0], InValue_B[1], InValue_B[2])

            print 'Calculation has been performed'
            print 'Offset value is {}, and dummy is {} \n'.format(InOffset, InDummy)
            val = (mVector_A + mVector_B)/2
            # ===


            #set output value
            sampleOutDataHandle.setMFloatVector(val)

            # as we recalculate all data for this output -
            # we should tell Maya that this attribute is recalculated
            # and all connected nodes should grab it
            sampleOutDataHandle.setClean()

        else:
            # this part makes Maya run compute from MPxNode class (which is empty)
            return OpenMaya.kUnknownParameter




"""
 * Register/Deregister node in the Maya system
"""


#initialize plug-in
def initializePlugin(plugin):

    pluginFn = OpenMaya.MFnPlugin(plugin, "Roman Volodin", "1.0", "Any")
    try:
        pluginFn.registerNode(  kPluginNodeName,        # the name of the node
                                kPluginNodeId,          # a unique node ID
                                MyNode.creator,         # function that creates an instance of the node
                                MyNode.initialize,      # function that creates input/output attributes
                                OpenMaya.MPxNode.kDependNode,# spicifies the node's type
                                'utility/general'       # node classification
                            )
    except:
        sys.stderr.write('Failed to register command: {}'.format(kPluginNodeName))
        raise



#Uninitialize plug-in
def uninitializePlugin(plugin):

    pluginFn = OpenMaya.MFnPlugin(plugin)
    try:
        pluginFn.deregisterNode(kPluginNodeId)
    except:
        sys.stderr.write('Failed to unregister command: {}'.format(kPluginNodeName))
        raise


"""
    * AETemplate controlls how your node appears in Maya's Attribute Editor
    * It's name should be built from:  AE{nodeName}Template like AEMyUselessNodeTemplate.mel
    * AETemapltes are used for every node you can see in Maya (even for built-in ones)
    * Rather than using usual mel UI commands, we use editorTemplate command all the time
        with different options
    * editorTemplate -addControl is the easiest way to add our custom control
    * if we change Template code, if we want to update it in maya -
        in AttributeEditor we can run Show->Set Global View->Default
"""


melCmd = '''
    //to update AETemplate in Maya - swith AE->show->setGlobalView
    global proc AEMyUselessNodeTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            // create collapsable form with controls
            editorTemplate -beginLayout "Useless Node Attributes" -collapse 0;
                editorTemplate -label "Input A" -addControl "inputA";
                editorTemplate -label "Input B" -addControl "inputB";
                editorTemplate -addSeparator;
                editorTemplate -label "Offset" -addControl "offset";
                editorTemplate -label "Dummy" -addControl "dummy";
            editorTemplate -endLayout;
            // here goes all attrs that are not manually added
            // using editorTemplate -addControl
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    }
'''
mel.eval(melCmd)