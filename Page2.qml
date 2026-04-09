import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 2.15

Item{
    id: page2root

        ColumnLayout {

            id: infoColumn
            anchors.fill: parent

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

                Text{
                        id: cltTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: mapTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: matTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: tpsTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: advTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: afrtgtTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: afrTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: battTextBox
                        Layout.fillWidth: true
                        color: "#800000"
                        text: "RPM: " + backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
    
                }

                Text{
                        id: gearTextBox
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
}