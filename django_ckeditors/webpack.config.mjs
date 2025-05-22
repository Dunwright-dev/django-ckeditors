// webpack.config.mjs
import path from 'path';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';
import { styles } from '@ckeditor/ckeditor5-dev-utils';
import { CKEditorTranslationsPlugin } from '@ckeditor/ckeditor5-dev-translations';
import MiniCssExtractPlugin from 'mini-css-extract-plugin';
import TerserPlugin from 'terser-webpack-plugin';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const require = createRequire(import.meta.url);

const isProduction = process.env.NODE_ENV === 'production';

export default {
    mode: isProduction ? 'production' : 'development',
    entry: './static/django_ckeditors/app.js',
    output: {
        path: path.resolve(__dirname, 'static/django_ckeditors/dist'),
        filename: isProduction 
            ? '[name].[contenthash].js'
            : '[name].js',
        chunkFilename: isProduction 
            ? '[name].[contenthash].chunk.js'
            : '[name].chunk.js',
        clean: true,
    },
    plugins: [
        new CKEditorTranslationsPlugin({
            language: 'en',
            additionalLanguages: 'all',
            buildAllTranslationsToSeparateFiles: true,
        }),
        new MiniCssExtractPlugin({
            filename: isProduction 
                ? '[name].[contenthash].css'
                : '[name].css',
            chunkFilename: isProduction
                ? '[name].[contenthash].chunk.css'
                : '[name].chunk.css'
        })
    ],
    module: {
        rules: [
            {
                test: /\.svg$/,
                use: ['raw-loader']
            },
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    {
                        loader: 'postcss-loader',
                        options: {
                            postcssOptions: styles.getPostCssConfig({
                                themeImporter: {
                                    themePath: require.resolve('@ckeditor/ckeditor5-theme-lark')
                                },
                                minify: isProduction
                            })
                        }
                    }
                ]
            }
        ]
    },
    optimization: {
        splitChunks: {
            chunks: 'all',
            cacheGroups: {
                ckeditor: {
                    test: /[\\/]node_modules[\\/]@ckeditor[\\/]/,
                    name: 'ckeditor',
                    chunks: 'all',
                    priority: 10,
                    minSize: 0,
                },
                vendor: {
                    test: /[\\/]node_modules[\\/](?!@ckeditor)/,
                    name: 'vendor',
                    chunks: 'all',
                    priority: 5,
                    minSize: 0,
                },
            },
        },
        minimize: isProduction,
        minimizer: [
            new TerserPlugin({
                terserOptions: {
                    format: {
                        comments: false,
                        beautify: !isProduction,
                    },
                    compress: {
                        drop_console: isProduction,
                        drop_debugger: isProduction,
                        pure_funcs: isProduction ? ['console.log', 'console.info'] : [],
                        passes: isProduction ? 2 : 1,
                    },
                    mangle: isProduction,
                },
                extractComments: false,
            }),
        ],
        sideEffects: true,
    },
    devtool: isProduction ? false : 'source-map',
    performance: {
        hints: isProduction ? "warning" : false,
        maxAssetSize: 1200000,
        maxEntrypointSize: 1500000,
    }
};
