import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 2.15

Item{
    id: page2root

        ColumnLayout {

            id: infoColumn
            anchors.fill: parent
            spacing: 0

            Rectangle{
                id: secondsValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: secondsTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Uptime: " + backend.seconds
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                }
            }

            Rectangle{
                id: rpmValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: rpmTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: cltValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: cltTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Coolant Temp: " + backend.clt
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: mapValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: mapTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Mass Airflow Pressure: " + backend.map
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: matValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: matTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Mass Airflow Temperature: " + backend.mat
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: tpsValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: tpsTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Throttle Position Sensor: " + backend.tps
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: advValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: advTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Timing advance: " + backend.adv_deg
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: afrtgtValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: afrtgtTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Air:Fuel Target: " + backend.afrtgt1
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: afrValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1
                Text{
                        id: afrTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Air:Fuel: " + backend.afr
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: battValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: battTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Battery Voltage: " + backend.batt
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }

            Rectangle{
                id: gearValueBox
                color: "transparent"
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.width * 0.1
                Layout.maximumHeight: Screen.width * 0.1

                Text{
                        id: gearTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "Gear: " + backend.gear
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }
            }


        }
}