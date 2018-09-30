import * as React from 'react';
import { ActivityIndicator, Text, View, StyleSheet,TouchableOpacity  } from 'react-native';
import { BarCodeScanner, Constants, Camera, Permissions } from 'expo';

// You can import from local files
import AssetExample from './components/AssetExample';

// or any pure javascript modules available in npm
import { Card } from 'react-native-elements'; // 0.19.1

export default class App extends React.Component {

    constructor(props){
        super(props);
        this.state ={ isLoading: true}
    }

    state = {
        hasCameraPermission: null,
        type: Camera.Constants.Type.back,
    };

    async componentWillMount() {
        const { status } = await Permissions.askAsync(Permissions.CAMERA);
        this.setState({ hasCameraPermission: status === 'granted' });
    }

    render() {
        const { hasCameraPermission } = this.state;
        if (hasCameraPermission === null) {
            return <View />;
        } else if (hasCameraPermission === false) {
            return <Text>No access to camera</Text>;
        } else {
            return (
                <View style={{ flex: 1 }}>
                <Camera style={{ flex: 1 }} type={this.state.type}>
                    <View
                    style={{
                        flex: 1,
                        backgroundColor: 'transparent',
                        flexDirection: 'row',
                    }}>
                    <BarCodeScanner onBarCodeScanned={this.handleBarCodeScanned} style={StyleSheet.absoluteFill}/>
                    <TouchableOpacity
                        style={{
                        flex: 0.1,
                        alignSelf: 'flex-end',
                        alignItems: 'center',
                        }}
                        onPress={() => {
                        this.setState({
                            type: this.state.type === Camera.Constants.Type.back
                            ? Camera.Constants.Type.front
                            : Camera.Constants.Type.back,
                        });
                        }}>
                        <Text
                        style={{ fontSize: 18, marginBottom: 10, color: 'white' }}>
                        {' '}Flip{' '}
                        </Text>
                        <Text style={styles.paragraph}>
                        Change code in the editor and watch it change on your phone! Save to get a shareable url.
                        </Text>
                    </TouchableOpacity>
                    </View>
                </Camera>
                </View>
            );
        }
    }

    handleBarCodeScanned = ({ type, data }) => {
        var url = `${data}`;
        alert(`Bar code with type ${type} and data ${data} has been scanned!`);
        return fetch('http://10.98.4.116:8000/nfce/data/', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ cpf: 1, link: url })// (`{ cpf: 1, link: ${url} }`),
        })
        .then((response => alert(`url: ${url}, Sucess:,${JSON.stringify(response)}`)))
        .catch(error => alert(`Error:, ${error}`))
    }
}

const styles = StyleSheet.create({
  paragraph: {
    margin: 24,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#34495e',
  },
});

