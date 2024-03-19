
"use strict";

let PlaceActionResult = require('./PlaceActionResult.js');
let MoveGroupActionGoal = require('./MoveGroupActionGoal.js');
let MoveGroupAction = require('./MoveGroupAction.js');
let MoveGroupSequenceFeedback = require('./MoveGroupSequenceFeedback.js');
let ExecuteTrajectoryActionFeedback = require('./ExecuteTrajectoryActionFeedback.js');
let MoveGroupSequenceResult = require('./MoveGroupSequenceResult.js');
let MoveGroupGoal = require('./MoveGroupGoal.js');
let ExecuteTrajectoryGoal = require('./ExecuteTrajectoryGoal.js');
let PickupFeedback = require('./PickupFeedback.js');
let MoveGroupSequenceActionGoal = require('./MoveGroupSequenceActionGoal.js');
let ExecuteTrajectoryFeedback = require('./ExecuteTrajectoryFeedback.js');
let PickupActionFeedback = require('./PickupActionFeedback.js');
let PlaceActionFeedback = require('./PlaceActionFeedback.js');
let PickupGoal = require('./PickupGoal.js');
let PlaceFeedback = require('./PlaceFeedback.js');
let PickupResult = require('./PickupResult.js');
let MoveGroupActionFeedback = require('./MoveGroupActionFeedback.js');
let PickupAction = require('./PickupAction.js');
let MoveGroupActionResult = require('./MoveGroupActionResult.js');
let ExecuteTrajectoryActionGoal = require('./ExecuteTrajectoryActionGoal.js');
let PlaceActionGoal = require('./PlaceActionGoal.js');
let ExecuteTrajectoryAction = require('./ExecuteTrajectoryAction.js');
let MoveGroupSequenceActionFeedback = require('./MoveGroupSequenceActionFeedback.js');
let ExecuteTrajectoryActionResult = require('./ExecuteTrajectoryActionResult.js');
let PickupActionResult = require('./PickupActionResult.js');
let ExecuteTrajectoryResult = require('./ExecuteTrajectoryResult.js');
let MoveGroupSequenceActionResult = require('./MoveGroupSequenceActionResult.js');
let MoveGroupSequenceAction = require('./MoveGroupSequenceAction.js');
let MoveGroupResult = require('./MoveGroupResult.js');
let PlaceAction = require('./PlaceAction.js');
let PlaceGoal = require('./PlaceGoal.js');
let MoveGroupFeedback = require('./MoveGroupFeedback.js');
let PickupActionGoal = require('./PickupActionGoal.js');
let PlaceResult = require('./PlaceResult.js');
let MoveGroupSequenceGoal = require('./MoveGroupSequenceGoal.js');
let MotionPlanResponse = require('./MotionPlanResponse.js');
let PlanningScene = require('./PlanningScene.js');
let PlanningSceneComponents = require('./PlanningSceneComponents.js');
let ConstraintEvalResult = require('./ConstraintEvalResult.js');
let JointLimits = require('./JointLimits.js');
let MotionSequenceRequest = require('./MotionSequenceRequest.js');
let GripperTranslation = require('./GripperTranslation.js');
let JointConstraint = require('./JointConstraint.js');
let AllowedCollisionMatrix = require('./AllowedCollisionMatrix.js');
let RobotTrajectory = require('./RobotTrajectory.js');
let CartesianTrajectoryPoint = require('./CartesianTrajectoryPoint.js');
let CollisionObject = require('./CollisionObject.js');
let OrientedBoundingBox = require('./OrientedBoundingBox.js');
let PlannerParams = require('./PlannerParams.js');
let GenericTrajectory = require('./GenericTrajectory.js');
let WorkspaceParameters = require('./WorkspaceParameters.js');
let DisplayRobotState = require('./DisplayRobotState.js');
let MotionPlanDetailedResponse = require('./MotionPlanDetailedResponse.js');
let MotionSequenceItem = require('./MotionSequenceItem.js');
let PositionIKRequest = require('./PositionIKRequest.js');
let PlanningSceneWorld = require('./PlanningSceneWorld.js');
let VisibilityConstraint = require('./VisibilityConstraint.js');
let ContactInformation = require('./ContactInformation.js');
let TrajectoryConstraints = require('./TrajectoryConstraints.js');
let MoveItErrorCodes = require('./MoveItErrorCodes.js');
let Constraints = require('./Constraints.js');
let PositionConstraint = require('./PositionConstraint.js');
let Grasp = require('./Grasp.js');
let MotionSequenceResponse = require('./MotionSequenceResponse.js');
let PlaceLocation = require('./PlaceLocation.js');
let CartesianPoint = require('./CartesianPoint.js');
let OrientationConstraint = require('./OrientationConstraint.js');
let LinkScale = require('./LinkScale.js');
let PlanningOptions = require('./PlanningOptions.js');
let AttachedCollisionObject = require('./AttachedCollisionObject.js');
let CostSource = require('./CostSource.js');
let KinematicSolverInfo = require('./KinematicSolverInfo.js');
let PlannerInterfaceDescription = require('./PlannerInterfaceDescription.js');
let LinkPadding = require('./LinkPadding.js');
let AllowedCollisionEntry = require('./AllowedCollisionEntry.js');
let ObjectColor = require('./ObjectColor.js');
let CartesianTrajectory = require('./CartesianTrajectory.js');
let MotionPlanRequest = require('./MotionPlanRequest.js');
let BoundingVolume = require('./BoundingVolume.js');
let RobotState = require('./RobotState.js');
let DisplayTrajectory = require('./DisplayTrajectory.js');

module.exports = {
  PlaceActionResult: PlaceActionResult,
  MoveGroupActionGoal: MoveGroupActionGoal,
  MoveGroupAction: MoveGroupAction,
  MoveGroupSequenceFeedback: MoveGroupSequenceFeedback,
  ExecuteTrajectoryActionFeedback: ExecuteTrajectoryActionFeedback,
  MoveGroupSequenceResult: MoveGroupSequenceResult,
  MoveGroupGoal: MoveGroupGoal,
  ExecuteTrajectoryGoal: ExecuteTrajectoryGoal,
  PickupFeedback: PickupFeedback,
  MoveGroupSequenceActionGoal: MoveGroupSequenceActionGoal,
  ExecuteTrajectoryFeedback: ExecuteTrajectoryFeedback,
  PickupActionFeedback: PickupActionFeedback,
  PlaceActionFeedback: PlaceActionFeedback,
  PickupGoal: PickupGoal,
  PlaceFeedback: PlaceFeedback,
  PickupResult: PickupResult,
  MoveGroupActionFeedback: MoveGroupActionFeedback,
  PickupAction: PickupAction,
  MoveGroupActionResult: MoveGroupActionResult,
  ExecuteTrajectoryActionGoal: ExecuteTrajectoryActionGoal,
  PlaceActionGoal: PlaceActionGoal,
  ExecuteTrajectoryAction: ExecuteTrajectoryAction,
  MoveGroupSequenceActionFeedback: MoveGroupSequenceActionFeedback,
  ExecuteTrajectoryActionResult: ExecuteTrajectoryActionResult,
  PickupActionResult: PickupActionResult,
  ExecuteTrajectoryResult: ExecuteTrajectoryResult,
  MoveGroupSequenceActionResult: MoveGroupSequenceActionResult,
  MoveGroupSequenceAction: MoveGroupSequenceAction,
  MoveGroupResult: MoveGroupResult,
  PlaceAction: PlaceAction,
  PlaceGoal: PlaceGoal,
  MoveGroupFeedback: MoveGroupFeedback,
  PickupActionGoal: PickupActionGoal,
  PlaceResult: PlaceResult,
  MoveGroupSequenceGoal: MoveGroupSequenceGoal,
  MotionPlanResponse: MotionPlanResponse,
  PlanningScene: PlanningScene,
  PlanningSceneComponents: PlanningSceneComponents,
  ConstraintEvalResult: ConstraintEvalResult,
  JointLimits: JointLimits,
  MotionSequenceRequest: MotionSequenceRequest,
  GripperTranslation: GripperTranslation,
  JointConstraint: JointConstraint,
  AllowedCollisionMatrix: AllowedCollisionMatrix,
  RobotTrajectory: RobotTrajectory,
  CartesianTrajectoryPoint: CartesianTrajectoryPoint,
  CollisionObject: CollisionObject,
  OrientedBoundingBox: OrientedBoundingBox,
  PlannerParams: PlannerParams,
  GenericTrajectory: GenericTrajectory,
  WorkspaceParameters: WorkspaceParameters,
  DisplayRobotState: DisplayRobotState,
  MotionPlanDetailedResponse: MotionPlanDetailedResponse,
  MotionSequenceItem: MotionSequenceItem,
  PositionIKRequest: PositionIKRequest,
  PlanningSceneWorld: PlanningSceneWorld,
  VisibilityConstraint: VisibilityConstraint,
  ContactInformation: ContactInformation,
  TrajectoryConstraints: TrajectoryConstraints,
  MoveItErrorCodes: MoveItErrorCodes,
  Constraints: Constraints,
  PositionConstraint: PositionConstraint,
  Grasp: Grasp,
  MotionSequenceResponse: MotionSequenceResponse,
  PlaceLocation: PlaceLocation,
  CartesianPoint: CartesianPoint,
  OrientationConstraint: OrientationConstraint,
  LinkScale: LinkScale,
  PlanningOptions: PlanningOptions,
  AttachedCollisionObject: AttachedCollisionObject,
  CostSource: CostSource,
  KinematicSolverInfo: KinematicSolverInfo,
  PlannerInterfaceDescription: PlannerInterfaceDescription,
  LinkPadding: LinkPadding,
  AllowedCollisionEntry: AllowedCollisionEntry,
  ObjectColor: ObjectColor,
  CartesianTrajectory: CartesianTrajectory,
  MotionPlanRequest: MotionPlanRequest,
  BoundingVolume: BoundingVolume,
  RobotState: RobotState,
  DisplayTrajectory: DisplayTrajectory,
};
