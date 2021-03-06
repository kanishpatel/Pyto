'''
Classes from the 'IDSFoundation' framework.
'''

try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None

    
IDSRegistrationControlChosenMetric = _Class('IDSRegistrationControlChosenMetric')
IDSSessionConnectedMetric = _Class('IDSSessionConnectedMetric')
IDSOpportunisticOptions = _Class('IDSOpportunisticOptions')
IDSStallDetector = _Class('IDSStallDetector')
IDSLocalDeliverySocketClosedMetric = _Class('IDSLocalDeliverySocketClosedMetric')
IDSRegistrationCompletedMetric = _Class('IDSRegistrationCompletedMetric')
IDSRemoteCredential = _Class('IDSRemoteCredential')
IDSEndpointTransparencyState = _Class('IDSEndpointTransparencyState')
IDSEngramKeyFetchMetric = _Class('IDSEngramKeyFetchMetric')
_IDSCurrentServerTimeProvider = _Class('_IDSCurrentServerTimeProvider')
IDSCurrentServerTimePair = _Class('IDSCurrentServerTimePair')
IDSCurrentServerTime = _Class('IDSCurrentServerTime')
IDSLogFormatter = _Class('IDSLogFormatter')
IDSSysdiagnoseLogCollector = _Class('IDSSysdiagnoseLogCollector')
IDSWiProxConnectionFailedMetric = _Class('IDSWiProxConnectionFailedMetric')
IDSSessionAcceptSentMetric = _Class('IDSSessionAcceptSentMetric')
IDSWiProxDidDisconnectFromPeerMetric = _Class('IDSWiProxDidDisconnectFromPeerMetric')
IDSKeyTransparencyTrustedDeviceEnrollmentMetric = _Class('IDSKeyTransparencyTrustedDeviceEnrollmentMetric')
IDSMissingMessageMetric = _Class('IDSMissingMessageMetric')
IDSLocalMessageTimedOutMetric = _Class('IDSLocalMessageTimedOutMetric')
IDSKeyTransparencyTrustedDeviceVerificationMetric = _Class('IDSKeyTransparencyTrustedDeviceVerificationMetric')
IDSProtobuf = _Class('IDSProtobuf')
IDSPayloadInspector = _Class('IDSPayloadInspector')
IDSCoreAnalyticsLogger = _Class('IDSCoreAnalyticsLogger')
IDSSessionInfoMetadataSerializer = _Class('IDSSessionInfoMetadataSerializer')
IDSLocalDeliveryMessageReceivedMetric = _Class('IDSLocalDeliveryMessageReceivedMetric')
IDSWiProxDidConnectToPeerMetric = _Class('IDSWiProxDidConnectToPeerMetric')
IDSSessionCompleted = _Class('IDSSessionCompleted')
IDSUDPLink = _Class('IDSUDPLink')
IDSRTCLogger = _Class('IDSRTCLogger')
IDSDeliveryControllerTimeMetric = _Class('IDSDeliveryControllerTimeMetric')
IDSCloudKitGroupServer = _Class('IDSCloudKitGroupServer')
IDSMMCSDownloadAuth = _Class('IDSMMCSDownloadAuth')
IDSXPCConnectionWrapper = _Class('IDSXPCConnectionWrapper')
IDSDependencyProvider = _Class('IDSDependencyProvider')
IDSWiProxDidSendDataMetric = _Class('IDSWiProxDidSendDataMetric')
IDSStunCandidatePair = _Class('IDSStunCandidatePair')
IDSInterfaceAddress = _Class('IDSInterfaceAddress')
IDSStunConnectionDataController = _Class('IDSStunConnectionDataController')
IDSCTAdapter = _Class('IDSCTAdapter')
IDSCTAdapterCache = _Class('IDSCTAdapterCache')
IDSCTSIM = _Class('IDSCTSIM')
IDSWRMExchange = _Class('IDSWRMExchange')
IDSWRMMetricContainer = _Class('IDSWRMMetricContainer')
IDSRemoteURLConnection = _Class('IDSRemoteURLConnection')
IDSMessageToDelete = _Class('IDSMessageToDelete')
IDSCTPNR = _Class('IDSCTPNR')
IDSCTPNRInfo = _Class('IDSCTPNRInfo')
IDSCTPNRResponseData = _Class('IDSCTPNRResponseData')
IDSCTPNRValidationMechanism = _Class('IDSCTPNRValidationMechanism')
IDSSessionStartedMetric = _Class('IDSSessionStartedMetric')
IDSMagnetCorruptionMetric = _Class('IDSMagnetCorruptionMetric')
IDSFoundationLog = _Class('IDSFoundationLog')
IDSQuickRelaySessionInfo = _Class('IDSQuickRelaySessionInfo')
IDSSendParameters = _Class('IDSSendParameters')
IDSMPConversationGroupSponsorPair = _Class('IDSMPConversationGroupSponsorPair')
IDSMPConversationGroup = _Class('IDSMPConversationGroup')
IDSStunCandidate = _Class('IDSStunCandidate')
IDSCertifiedDeliveryContext = _Class('IDSCertifiedDeliveryContext')
IDSRegistrationAccountStatusMetric = _Class('IDSRegistrationAccountStatusMetric')
IDSQueryKeyTransparencyContext = _Class('IDSQueryKeyTransparencyContext')
IDSSessionInvitationReceivedMetric = _Class('IDSSessionInvitationReceivedMetric')
IDSSessionEndedMetric = _Class('IDSSessionEndedMetric')
IDSLocalMessageDeliveryConnectionResetMetric = _Class('IDSLocalMessageDeliveryConnectionResetMetric')
IDSLegacyDeviceMessageProtectionCypher = _Class('IDSLegacyDeviceMessageProtectionCypher')
IDSSOSLogger = _Class('IDSSOSLogger')
IDSConversationGroupCypher = _Class('IDSConversationGroupCypher')
IDSSocketPairResourceTransferReceiver = _Class('IDSSocketPairResourceTransferReceiver')
IDSSocketPairMessage = _Class('IDSSocketPairMessage')
IDSSocketPairServiceMapMessage = _Class('IDSSocketPairServiceMapMessage')
IDSSocketPairResourceTransferSender = _Class('IDSSocketPairResourceTransferSender')
IDSSocketPairFragmentedMessage = _Class('IDSSocketPairFragmentedMessage')
IDSSocketPairProtobufMessage = _Class('IDSSocketPairProtobufMessage')
IDSSocketPairAppAckMessage = _Class('IDSSocketPairAppAckMessage')
IDSSocketPairKeepAliveMessage = _Class('IDSSocketPairKeepAliveMessage')
IDSSocketPairAckMessage = _Class('IDSSocketPairAckMessage')
IDSSocketPairExpiredAckMessage = _Class('IDSSocketPairExpiredAckMessage')
IDSSocketPairOTRMessage = _Class('IDSSocketPairOTRMessage')
IDSSocketPairOTREncryptedMessage = _Class('IDSSocketPairOTREncryptedMessage')
IDSSocketPairEncryptedMessage = _Class('IDSSocketPairEncryptedMessage')
IDSSocketPairHandshake = _Class('IDSSocketPairHandshake')
IDSSocketPairDataMessage = _Class('IDSSocketPairDataMessage')
IDSSocketPairResourceTransferMessage = _Class('IDSSocketPairResourceTransferMessage')
IDSSocketPairErrorMessage = _Class('IDSSocketPairErrorMessage')
IDSSocketPairLocationShareOfferCommand = _Class('IDSSocketPairLocationShareOfferCommand')
IDSSocketPairGenericGroupMessageCommand = _Class('IDSSocketPairGenericGroupMessageCommand')
IDSSocketPairGenericCommandMessage = _Class('IDSSocketPairGenericCommandMessage')
IDSSocketPairReflectedDeliveryReceipt = _Class('IDSSocketPairReflectedDeliveryReceipt')
IDSSocketPairSavedReceipt = _Class('IDSSocketPairSavedReceipt')
IDSSocketPairPlayedReceipt = _Class('IDSSocketPairPlayedReceipt')
IDSSocketPairAttachmentMessage = _Class('IDSSocketPairAttachmentMessage')
IDSSocketPairReadReceipt = _Class('IDSSocketPairReadReceipt')
IDSSocketPairDeliveryReceipt = _Class('IDSSocketPairDeliveryReceipt')
IDSSocketPairTextMessage = _Class('IDSSocketPairTextMessage')
IDSSocketPairProxyIncomingNiceMessage = _Class('IDSSocketPairProxyIncomingNiceMessage')
IDSSocketPairProxyOutgoingNiceMessage = _Class('IDSSocketPairProxyOutgoingNiceMessage')
IDSSocketPairSMSFailure = _Class('IDSSocketPairSMSFailure')
IDSSocketPairSMSReadReceipt = _Class('IDSSocketPairSMSReadReceipt')
IDSSocketPairSMSDeliveryReceipt = _Class('IDSSocketPairSMSDeliveryReceipt')
IDSSocketPairSMSDownloadOutgoing = _Class('IDSSocketPairSMSDownloadOutgoing')
IDSSocketPairSMSOutgoing = _Class('IDSSocketPairSMSOutgoing')
IDSSocketPairSMSTextDownloadMessage = _Class('IDSSocketPairSMSTextDownloadMessage')
IDSSocketPairSMSTextMessage = _Class('IDSSocketPairSMSTextMessage')
IDSSocketPairSessionEndMessage = _Class('IDSSocketPairSessionEndMessage')
IDSSocketPairSessionReinitiateMessage = _Class('IDSSocketPairSessionReinitiateMessage')
IDSSocketPairSessionMessage = _Class('IDSSocketPairSessionMessage')
IDSSocketPairSessionCancelMessage = _Class('IDSSocketPairSessionCancelMessage')
IDSSocketPairSessionDeclineMessage = _Class('IDSSocketPairSessionDeclineMessage')
IDSSocketPairSessionAcceptMessage = _Class('IDSSocketPairSessionAcceptMessage')
IDSSocketPairSessionInvitationMessage = _Class('IDSSocketPairSessionInvitationMessage')
IDSSocketPairDictionaryMessage = _Class('IDSSocketPairDictionaryMessage')
IDSOpportunisticData = _Class('IDSOpportunisticData')
IDSWRMLinkRecommendationMetric = _Class('IDSWRMLinkRecommendationMetric')
IDSCloudKitTransportLogChangeToken = _Class('IDSCloudKitTransportLogChangeToken')
IDSCloudKitTransportLogMessage = _Class('IDSCloudKitTransportLogMessage')
IDSCloudKitTransportLog = _Class('IDSCloudKitTransportLog')
IDSEndpoint = _Class('IDSEndpoint')
IDSWiProxConnectionSuccessMetric = _Class('IDSWiProxConnectionSuccessMetric')
IDSSOSMetric = _Class('IDSSOSMetric')
IDSSessionAcceptReceivedMetric = _Class('IDSSessionAcceptReceivedMetric')
IDSRegistrationAuthenticationParametersReceivedMetric = _Class('IDSRegistrationAuthenticationParametersReceivedMetric')
IDSSockAddrWrapper = _Class('IDSSockAddrWrapper')
IDSLocalDeliveryMessageDeliveredMetric = _Class('IDSLocalDeliveryMessageDeliveredMetric')
IDSCloudKitKeyElectionStoreItem = _Class('IDSCloudKitKeyElectionStoreItem')
IDSCloudKitKeyElectionStore = _Class('IDSCloudKitKeyElectionStore')
IDSSessionReinitiateStartedMetric = _Class('IDSSessionReinitiateStartedMetric')
IDSQRAllocationMetric = _Class('IDSQRAllocationMetric')
IDSAutoBugCapture = _Class('IDSAutoBugCapture')
IDSTapToRadar = _Class('IDSTapToRadar')
IDSTapToRadarContext = _Class('IDSTapToRadarContext')
IDSTapToRadarRequest = _Class('IDSTapToRadarRequest')
IDSServerCertificate = _Class('IDSServerCertificate')
IDSLocalDeliveryMessageSentMetric = _Class('IDSLocalDeliveryMessageSentMetric')
IDSAWDLogging = _Class('IDSAWDLogging')
IDSAuthenticationCertificate = _Class('IDSAuthenticationCertificate')
IDSSessionCancelSentMetric = _Class('IDSSessionCancelSentMetric')
IDSCertifiedDeliveryReplayKey = _Class('IDSCertifiedDeliveryReplayKey')
IDSMPIdentity = _Class('IDSMPIdentity')
IDSMPPublicServiceIdentitySigning = _Class('IDSMPPublicServiceIdentitySigning')
IDSMPFullServiceIdentitySigning = _Class('IDSMPFullServiceIdentitySigning')
IDSMPPublicServiceIdentityAdmin = _Class('IDSMPPublicServiceIdentityAdmin')
IDSMPFullServiceIdentityAdmin = _Class('IDSMPFullServiceIdentityAdmin')
IDSMPPublicDeviceIdentity = _Class('IDSMPPublicDeviceIdentity')
IDSMPFullDeviceIdentity = _Class('IDSMPFullDeviceIdentity')
IDSMPPublicAccountIdentityCluster = _Class('IDSMPPublicAccountIdentityCluster')
IDSMPFullAccountIdentityCluster = _Class('IDSMPFullAccountIdentityCluster')
IDSMPPublicAccountIdentity = _Class('IDSMPPublicAccountIdentity')
IDSMPFullAccountIdentity = _Class('IDSMPFullAccountIdentity')
IDSMPPublicLegacyIdentity = _Class('IDSMPPublicLegacyIdentity')
IDSMPFullLegacyIdentity = _Class('IDSMPFullLegacyIdentity')
IDSSessionReinitiateRequestedMetric = _Class('IDSSessionReinitiateRequestedMetric')
IDSMPConversationKey = _Class('IDSMPConversationKey')
IDSMessageContext = _Class('IDSMessageContext')
IDSNWPathUtils = _Class('IDSNWPathUtils')
IDSWiFiSetupAttemptMetric = _Class('IDSWiFiSetupAttemptMetric')
IDSNGMMessageHasher = _Class('IDSNGMMessageHasher')
IDSNGMKeyRollingTicket = _Class('IDSNGMKeyRollingTicket')
IDSNGMProtocolVersion = _Class('IDSNGMProtocolVersion')
IDSNGMPublicDeviceIdentity = _Class('IDSNGMPublicDeviceIdentity')
IDSNGMFullDeviceIdentity = _Class('IDSNGMFullDeviceIdentity')
IDSOTRSessionNegotiationMetric = _Class('IDSOTRSessionNegotiationMetric')
IDSStunMessage = _Class('IDSStunMessage')
IDSDelegateInfo = _Class('IDSDelegateInfo')
IDSGlobalLinkMessage = _Class('IDSGlobalLinkMessage')
IDSURI = _Class('IDSURI')
IDSCKAccountInfo = _Class('IDSCKAccountInfo')
IDSCKSubscription = _Class('IDSCKSubscription')
IDSCKRecordZoneSubscription = _Class('IDSCKRecordZoneSubscription')
IDSCKQuerySubscription = _Class('IDSCKQuerySubscription')
IDSCKNotificationInfo = _Class('IDSCKNotificationInfo')
IDSCKNotification = _Class('IDSCKNotification')
IDSCKRecordZoneNotification = _Class('IDSCKRecordZoneNotification')
IDSCKFetchRecordZoneChangesOptions = _Class('IDSCKFetchRecordZoneChangesOptions')
IDSCKServerChangeToken = _Class('IDSCKServerChangeToken')
IDSCKRecordZone = _Class('IDSCKRecordZone')
IDSCKRecordZoneID = _Class('IDSCKRecordZoneID')
IDSCKDatabaseOperation = _Class('IDSCKDatabaseOperation')
IDSCKModifySubscriptionsOperation = _Class('IDSCKModifySubscriptionsOperation')
IDSCKFetchRecordZonesOperation = _Class('IDSCKFetchRecordZonesOperation')
IDSCKModifyRecordZonesOperation = _Class('IDSCKModifyRecordZonesOperation')
IDSCKFetchRecordsOperation = _Class('IDSCKFetchRecordsOperation')
IDSCKFetchRecordZoneChangesOperation = _Class('IDSCKFetchRecordZoneChangesOperation')
IDSCKQueryOperation = _Class('IDSCKQueryOperation')
IDSCKModifyRecordsOperation = _Class('IDSCKModifyRecordsOperation')
IDSCKQuery = _Class('IDSCKQuery')
IDSCKRecordID = _Class('IDSCKRecordID')
IDSCKRecord = _Class('IDSCKRecord')
IDSCKDatabase = _Class('IDSCKDatabase')
IDSCKContainer = _Class('IDSCKContainer')
IDSAWDLogger = _Class('IDSAWDLogger')
IDSLocalMessageRTTMetric = _Class('IDSLocalMessageRTTMetric')
IDSPushHandler = _Class('IDSPushHandler')
IDSPushHandlerContext = _Class('IDSPushHandlerContext')
IDSDestinationStrings = _Class('IDSDestinationStrings')
IDSQRParticipantStreams = _Class('IDSQRParticipantStreams')
IDSMagnetDataCorruptionRecoveryTimeInMsMetric = _Class('IDSMagnetDataCorruptionRecoveryTimeInMsMetric')
IDSDeviceIdentity = _Class('IDSDeviceIdentity')
IDSPublicDeviceIdentity = _Class('IDSPublicDeviceIdentity')
IDSGlobalLinkBlocks = _Class('IDSGlobalLinkBlocks')
IDSBaseSocketPairConnection = _Class('IDSBaseSocketPairConnection')
IDSSessionDeclineReceivedMetric = _Class('IDSSessionDeclineReceivedMetric')
IDSLocalMessageSentMetric = _Class('IDSLocalMessageSentMetric')
IDSEndpointCapabilities = _Class('IDSEndpointCapabilities')
IDSAccountKeyHistory = _Class('IDSAccountKeyHistory')
IDSCloudKitKeyValueStore = _Class('IDSCloudKitKeyValueStore')
IDSCellularLinkMonitor = _Class('IDSCellularLinkMonitor')
IDSRateLimiter = _Class('IDSRateLimiter')
IDSNegativeInfo = _Class('IDSNegativeInfo')
IDSTransactionQueue = _Class('IDSTransactionQueue')
IDSTransactionQueueTransaction = _Class('IDSTransactionQueueTransaction')
IDSRegistrationKeychainReader = _Class('IDSRegistrationKeychainReader')
IDSRegistrationCertificate = _Class('IDSRegistrationCertificate')
IDSDeliveryContext = _Class('IDSDeliveryContext')
IDSServiceProperties = _Class('IDSServiceProperties')
IDSQuickRelayMetric = _Class('IDSQuickRelayMetric')
IDSHandle = _Class('IDSHandle')
IDSSessionCanceledMetric = _Class('IDSSessionCanceledMetric')
IDSSessionInvitationSentMetric = _Class('IDSSessionInvitationSentMetric')
IDSAccountIdentity = _Class('IDSAccountIdentity')
IDSPublicAccountIdentity = _Class('IDSPublicAccountIdentity')
IDSTCPLink = _Class('IDSTCPLink')
IDSServiceDelegateProperties = _Class('IDSServiceDelegateProperties')
IDSDestination = _Class('IDSDestination')
IDSDestinationPushToken = _Class('IDSDestinationPushToken')
IDSDestinationDevice = _Class('IDSDestinationDevice')
IDSDestinationDefaultPairedDevice = _Class('IDSDestinationDefaultPairedDevice')
IDSDestinationURI = _Class('IDSDestinationURI')
IDSDestinationSentinelSelfAlias = _Class('IDSDestinationSentinelSelfAlias')
IDSDestinationEngram = _Class('IDSDestinationEngram')
IDSDestinationComposite = _Class('IDSDestinationComposite')
IDSGroupSessionActiveParticipant = _Class('IDSGroupSessionActiveParticipant')
IDSBaseMessage = _Class('IDSBaseMessage')
IDSMessage = _Class('IDSMessage')
IDSCertifiedDeliveryReceiptMessage = _Class('IDSCertifiedDeliveryReceiptMessage')
IDSMMCSAccessRequestMessage = _Class('IDSMMCSAccessRequestMessage')
IDSSessionReinitiateConnectedMetric = _Class('IDSSessionReinitiateConnectedMetric')
IDSRegisteredDevice = _Class('IDSRegisteredDevice')
IDSCloudMessagingLinkReEstablishedMetric = _Class('IDSCloudMessagingLinkReEstablishedMetric')
IDSServerBag = _Class('IDSServerBag')
IDSIDSServerBag = _Class('IDSIDSServerBag')
IDSCourierServerBag = _Class('IDSCourierServerBag')
IDSGlobalLink = _Class('IDSGlobalLink')
IDSGFTGL = _Class('IDSGFTGL')
IDSNonFTGL = _Class('IDSNonFTGL')
IDSFTGL = _Class('IDSFTGL')
IDSPopupPrompt = _Class('IDSPopupPrompt')
IDSSessionDeclineSentMetric = _Class('IDSSessionDeclineSentMetric')
IDSPNRMetric = _Class('IDSPNRMetric')
IDSMPPublicDeviceIdentityContainer = _Class('IDSMPPublicDeviceIdentityContainer')
IDSMPFullDeviceIdentityContainer = _Class('IDSMPFullDeviceIdentityContainer')
IDSCloudKitContainer = _Class('IDSCloudKitContainer')
IDSGroupSessionParticipantUpdate = _Class('IDSGroupSessionParticipantUpdate')
IDSLocalMessageDeliveryServiceNotCompatibleMetric = _Class('IDSLocalMessageDeliveryServiceNotCompatibleMetric')
IDSLocalDeliverySocketOpenedMetric = _Class('IDSLocalDeliverySocketOpenedMetric')
IDSAggregateMessageSendCheckpointTrace = _Class('IDSAggregateMessageSendCheckpointTrace')
IDSPeerMessageCheckpointTrace = _Class('IDSPeerMessageCheckpointTrace')
IDSIncomingMessageCheckpointTrace = _Class('IDSIncomingMessageCheckpointTrace')
IDSOutgoingMessageCheckpointTrace = _Class('IDSOutgoingMessageCheckpointTrace')
